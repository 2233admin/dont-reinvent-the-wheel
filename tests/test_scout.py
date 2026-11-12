"""Offline tests for scout.py: no network needed.  Run: python3 -m unittest discover -s tests"""
import importlib.util
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "scout", os.path.join(HERE, "..", "skills", "dont-reinvent-the-wheel", "scripts", "scout.py"))
scout = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scout)

README = """# seedtool
[![ci](https://img.shields.io/badge/x-y-green)](https://github.com/acme/seedtool/actions)

Built on [libfoo](https://github.com/foo/libfoo).

```bash
git clone https://github.com/acme/in-a-code-block
```

## Alternatives
- [othertool](https://github.com/Bar/OtherTool.git) - does the same in Go
- https://github.com/baz/third/issues/12
- see also https://github.com/sponsors/someone

## 类似项目
- [中文项目](https://github.com/zh/xiangmu)

## License
MIT, see https://github.com/acme/seedtool/blob/main/LICENSE
"""


class RepoKey(unittest.TestCase):
    def test_normalises(self):
        self.assertEqual(scout.repo_key("https://github.com/Bar/OtherTool.git"), "github.com/bar/othertool")
        self.assertEqual(scout.repo_key("git+ssh://git@github.com:a/b.git"), "github.com/a/b")
        self.assertEqual(scout.repo_key("https://github.com/baz/third/issues/12"), "github.com/baz/third")

    def test_rejects_non_repos(self):
        self.assertIsNone(scout.repo_key("https://github.com/sponsors/someone"))
        self.assertIsNone(scout.repo_key("https://example.com/a/b"))
        self.assertIsNone(scout.repo_key(None))


class ParseReadme(unittest.TestCase):
    def setUp(self):
        self.found = {c["key"]: c for c in scout.parse_readme(README, "github.com/acme/seedtool")}

    def test_finds_links_and_skips_self_badges_code(self):
        self.assertEqual(set(self.found), {
            "github.com/foo/libfoo", "github.com/bar/othertool",
            "github.com/baz/third", "github.com/zh/xiangmu"})

    def test_flags_related_headings_in_english_and_chinese(self):
        self.assertTrue(self.found["github.com/bar/othertool"]["flagged"])
        self.assertTrue(self.found["github.com/zh/xiangmu"]["flagged"])
        self.assertFalse(self.found["github.com/foo/libfoo"]["flagged"])

    def test_flagged_come_first(self):
        ordered = scout.parse_readme(README, "github.com/acme/seedtool")
        self.assertTrue(ordered[0]["flagged"])
        self.assertFalse(ordered[-1]["flagged"])


class Rounds(unittest.TestCase):
    def test_new_seen_keep_and_saturation(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "s.json")
            a = [{"key": "github.com/a/a"}, {"key": "github.com/b/b"}]
            info = scout.apply_state(path, a, "r1")
            self.assertEqual((info["round"], info["new"]), (1, 2))
            scout.keep(path, ["a/a"])
            self.assertFalse(scout.status(path)["saturated"])

            again = [{"key": "github.com/a/a"}, {"key": "npm:c"}]
            info = scout.apply_state(path, again, "r2")
            self.assertEqual(info["new"], 1)
            self.assertFalse(again[0]["new"])
            self.assertTrue(again[1]["new"])
            self.assertFalse(scout.status(path)["saturated"])   # one quiet round

            scout.apply_state(path, [{"key": "npm:d"}], "r3")
            st = scout.status(path)
            self.assertEqual(st["rounds_since_shortlist_grew"], 2)
            self.assertTrue(st["saturated"])                    # two quiet rounds

            scout.keep(path, ["npm:d"])                         # shortlist grew in round 3
            self.assertFalse(scout.status(path)["saturated"])

    def test_empty_shortlist_is_never_saturated(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "s.json")
            for i in range(3):
                scout.apply_state(path, [{"key": f"npm:{i}"}], f"r{i}")
            self.assertFalse(scout.status(path)["saturated"])


if __name__ == "__main__":
    unittest.main()
