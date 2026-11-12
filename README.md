# 别重复造轮子 · dont-reinvent-the-wheel

[中文](README.zh-CN.md)

<p align="center">
  <img src="docs/assets/banner.svg" width="840" alt="Monochrome ASCII megastructure: endless pillars, trusses and pipes drawn in text characters. A tiny pixel figure in an amber hard hat walks along a bridge, planning to build a wheel, and stops in front of a colossal wheel that has been turning there all along. Caption: it was already here. Verdict: Adopt.">
</p>

An agent skill for the moment you are about to build something. It finds what already
exists, including the things you would never find because you don't know what they are
called.

```text
 need -> name it 6 ways -> find a seed -> snowball -> quiet? -yes-> read <=5 -> verdict -> report
              ^                                         |
              +------------------- no ------------------+
```

## The problem

"Search GitHub first" usually fails for one reason: the thing exists under a name you
didn't search for. While surveying prior art for this very skill we found the same idea
published as `search-first`, `prior-art`, `idea-check`, `wheelspotter`, `github-scout`,
`skill-scout`, `dont-reinvent`, `programming-advisor` and `skill-hunter`. No keyword finds
them all, and it took four rounds of searching to turn them up.

## What it does

1. **Names the need several ways before searching.** The trade term, your own words,
   another language, the category, a known product, the first line a README would open
   with, and the complaint people make when the tool is missing.
2. **Finds one seed, then snowballs.** It reads the seed's own "Alternatives" section, its
   topics and its awesome-list neighbours. Authors know their competition better than a
   search engine does.
3. **Stops when the search goes quiet.** Two rounds in a row that add nothing to the
   shortlist. A script keeps count, so "I searched enough" is a number.
4. **Reads before it judges.** At most five candidates, opened properly: README, a core
   source file, the issue tracker, what access it asks for, how it updates.
5. **Leaves a dated report** in `docs/prior-art/`, with the terms and sources used, so the
   next survey of the topic starts from this one.

Steps 2 and 3 are the part we built. The rest is assembled from ideas other skills had
first; see [Borrowed from](#borrowed-from).

## What you get back

One verdict per part of the need. This is the real table from
[this skill's own survey](docs/prior-art/dont-reinvent-the-wheel.md):

| Part | Verdict | Project |
|---|---|---|
| Finding the user's own earlier work | Adopt (by reference) | prior-work-retrieval |
| Fetching results from several sources | Compose | public registry and search APIs |
| Sizing the survey, naming, screening, verdict rules | Extend (ideas) | search-first, dont-reinvent, skill-scout, programming-advisor |
| Seed, snowball, stop rule, dated report | Build | — |

The verdicts are **Adopt, Extend, Compose, Build** and **Keep**. A Build verdict has to
complete the sentence "Existing X cannot do ___ because ___." "To learn" and "for fun" are
fine reasons to build, as long as they are written down as the reason.

## It runs beside a prototype, not before one

The survey is not a gate. Building is cheap now, so start the rough prototype and run the
survey at the same time. What the prototype teaches you (the terms, the libraries, the
error messages) goes back in as search terms. The survey only has to finish before stopping
gets expensive: before other people depend on the thing, before a week has gone into it,
before it is announced.

## Install

The skill is the folder `skills/dont-reinvent-the-wheel`. Copy it into your agent's skills
directory:

```bash
git clone https://github.com/2233admin/dont-reinvent-the-wheel
cp -r dont-reinvent-the-wheel/skills/dont-reinvent-the-wheel ~/.claude/skills/   # Claude Code
```

Or with the `skills` CLI:

```bash
npx skills add 2233admin/dont-reinvent-the-wheel
```

It needs web search or network access from a shell. The bundled script needs Python 3.8+
and nothing else.

## Use

Ask the way you normally would:

> Before we start — is there already something that does this?
>
> 我想做个从 AI 平台抓提示词和封面的素材库插件，先查查有没有现成的。

Or drive the script yourself:

```bash
cd skills/dont-reinvent-the-wheel
S=.prior-art/link-checker.json

python3 scripts/scout.py check                                  # which sources can be reached
python3 scripts/scout.py search  --state $S -t "markdown link checker" \
        -t "dead link checker" -t "死链检查" --channels github,hn,npm
python3 scripts/scout.py keep    --state $S lycheeverse/lychee  # worth a closer look
python3 scripts/scout.py related --state $S lycheeverse/lychee  # what its README points to
python3 scripts/scout.py status  --state $S                     # has the search gone quiet?
```

| Command | What it does |
|---|---|
| `check` | One tiny query per source; prints which ones answer |
| `search` | Sends every term to every source and merges the results; what several terms agree on comes first |
| `keep` | Adds candidates to the shortlist |
| `related` | Lists the projects a seed's README names, "Alternatives" sections first |
| `status` | Rounds so far, the shortlist, and whether two rounds have passed without it growing |

Stars and downloads are shown but never used for ranking. A source that fails is reported
as not searched, never as empty. Set `GITHUB_TOKEN` to raise GitHub's search rate limit.

## Borrowed from

This skill would be a poor advertisement for itself if it had been written from scratch.
After the first draft we read twelve similar projects and took what they did better. Ideas
only; no text was copied.

| Idea | From |
|---|---|
| Split the need into parts; Build carries the burden of proof; name what rules a candidate out; record the terms searched | [search-first](https://github.com/shimo4228/search-first) |
| Size the survey to what is at stake; search the complaint, not just the name; open a named candidate and still check two neighbours; the Keep verdict; record source, version and update path; check what access a candidate asks for | [dont-reinvent](https://github.com/LucioLiu/dont-reinvent) |
| Check which sources are reachable first; the Compose verdict | [search-first](https://github.com/affaan-m/everything-claude-code) in everything-claude-code |
| Grep installed skills by description; read a skill's commands before recommending it | [skill-scout](https://github.com/affaan-m/everything-claude-code) |
| Hosted services count as candidates; a higher bar for auth, crypto and payments | [programming-advisor](https://github.com/gaupoit/programming-advisor) |
| A failed source is not an empty one; "read" and "seen" are different claims | [prior-work-retrieval](https://github.com/daymade/claude-code-skills) |
| Say so when little was found; stop at the verdict | [prior-art](https://github.com/bendrucker/claude) |
| Ask why abandoned projects stopped | [research](https://github.com/MrToxy/claude-skills) |
| Where to look for a code pattern, as opposed to a project | [librarian](https://github.com/roerohan/skills) |
| Several sources in parallel | [idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp) |

## Alternatives

Several of these do things this skill does not. Details and dates are in
[the survey](docs/prior-art/dont-reinvent-the-wheel.md).

| Project | Use it instead when |
|---|---|
| [search-first](https://github.com/shimo4228/search-first) | You already know what to search for and need a rigorous adopt-or-build decision. Its verdict rules are stricter than ours. The two work well together: this skill to find, search-first to decide. |
| [dont-reinvent](https://github.com/LucioLiu/dont-reinvent) | The thing you are about to make is itself a skill or a reusable team capability, and you want it registered and kept up to date afterwards. Note its noncommercial licence. |
| [prior-work-retrieval](https://github.com/daymade/claude-code-skills) | The question is "have *we* done this before?" — your own code, documents and past conversations. |
| [programming-advisor](https://github.com/gaupoit/programming-advisor) | You want a build-versus-buy cost comparison and an integration plan. |
| [idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp) | You want a quick score for how crowded an idea is. Also usable as this skill's first pass. |
| [AutoSearch](https://github.com/0xmariowu/autosearch) | You need reach into many sources, including Chinese-language ones. A search backend this skill can sit on top of. |

## Limits

- Version 0.1. No agent has yet run the whole procedure on a real task, and it has not
  been compared against working without it.
- The `github` source has not been run against the live API; the other four have.
- The stop rule depends on the agent marking what is worth keeping. The script counts; it
  does not judge relevance.
- PyPI has no search API. The `pypi` source only checks whether a package is named after the
  term.
- Package registries are poor at concept queries. Use them for library-shaped needs.
- Most of this skill is other people's ideas, put together so they can be used as one
  thing. That is on purpose. The parts we added ourselves are the snowball step and the
  stop counter.

## Development

```bash
python3 -m unittest discover -s tests
```

## Licence

MIT
