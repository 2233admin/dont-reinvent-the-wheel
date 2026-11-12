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
first; they are credited in [the survey](docs/prior-art/dont-reinvent-the-wheel.md).

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
