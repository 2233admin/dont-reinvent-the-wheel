# Prior art: dont-reinvent-the-wheel（别重复造轮子）

- Date: 2026-11-12
- Mode: deep
- Searches used: 7 web searches; 12 projects opened and read
- Saturated: **no** — each of the four search rounds added a project to the shortlist

This is the survey run for this skill itself, in the skill's own report format. The first
pass read five projects and only listed the rest; a second pass the same day read seven
more and folded what they do well into the skill.

## Need

For a developer or coding agent about to build something: given a rough description of the
idea, find the existing projects that already do it, including ones described in different
words or another language, and end with a decision on whether to build.

Constraints: must work as a plain Agent Skill folder in any host that reads `SKILL.md`; no
required service, account or API key; permissive licence.

## Verdict

| Part | Verdict | Project | Why |
|---|---|---|---|
| Finding the user's own earlier work | Adopt (by reference) | prior-work-retrieval | Far more thorough than a step here could be. This skill keeps a light "look at home" step and points to it. |
| Fetching results from several sources | Compose | public registry and search APIs | A short standard-library script covers it. idea-reality-mcp and AutoSearch can serve as the first pass when installed. |
| Sizing the survey, naming, screening, verdict rules | Extend (ideas) | search-first, dont-reinvent, skill-scout, programming-advisor | Each had pieces this skill lacked. They were rewritten in our own words and credited in the README. |
| Seed, snowball, stop rule, dated report | Build | — | See below. |

**Build sentence.** The twelve projects we opened cannot tell a searcher when to stop or
lead them from one find to its neighbours, because none of them follows a found project's
own list of alternatives and none keeps a count of whether the search is still producing.
Several expand the search terms (dont-reinvent, idea-reality-mcp) and several decide
rigorously (search-first), so those parts were borrowed, not built.

Rough size of what was built: one script of about 490 lines, a 245-line SKILL.md and two reference
files. To maintain: the five source adapters in the script, which break when an API changes.

**How thin this is.** The new part is two steps and a state file. If search-first or
dont-reinvent added a snowball step and a stop counter, most of the reason for a separate
skill would be gone. It was kept separate for two reasons, both judgments: search-first is
published by a one-way sync from its author's private setup (`scripts/sync-from-local.sh`),
so flow changes may not be accepted from outside; and dont-reinvent is under a
noncommercial licence, which rules out building on it for an MIT project.

## Read

Fetched on 2026-11-12. "Read" means the SKILL.md in full unless noted.

| Project | Link | Covers | Lacks | Licence | Last commit | Cost to adopt | Access it needs |
|---|---|---|---|---|---|---|---|
| search-first (shimo4228) | https://github.com/shimo4228/search-first | Splits a plan into parts; checks the repo first; stop rule per question type; Adopt is the default and Build must say what rules each candidate out; report records the terms searched | No alternative-names step; no following of a project's listed alternatives; Full mode tied to the author's setup (ADR references, a `researcher` agent, hooks) | MIT | 2026-11-01 | Copy one folder; Quick mode works anywhere | Web search |
| dont-reinvent (LucioLiu) | https://github.com/LucioLiu/dont-reinvent | Sizes the survey to the change; builds queries from outcome, synonyms, adjacent categories and failure patterns; eight comparison dimensions including permissions and update path; adopt / adapt / compose / keep / build; registers what was installed and how it updates | Ships no search of its own; no snowballing; no stop rule; aimed at skills and reusable capabilities more than libraries | PolyForm Noncommercial 1.0.0 | 2026-08-13 | Copy one file; expects a team "shelf" directory | Whatever search the host provides |
| search-first (everything-claude-code) | https://github.com/affaan-m/everything-claude-code | Checks which search channels are available first; npm/PyPI, MCP, skills, GitHub; adopt / extend / compose / build; names "silent skipping" as a failure | Keyword search only; no names step; no stop rule; hands the search to a generic sub-agent | MIT | 2026-11-06 | Part of a large collection | Web search, optional `gh` |
| skill-scout (everything-claude-code) | https://github.com/affaan-m/everything-claude-code | For skills only: greps installed skills by name and description; `gh search`; vets a skill's commands before recommending it; use / fork / create | Skills only; three web queries at most; nothing saved | MIT | 2026-11-06 | Part of a large collection | Local files, optional `gh` |
| programming-advisor (gaupoit) | https://github.com/gaupoit/programming-advisor | Build-versus-buy: includes hosted services; cost comparison over time; a higher bar for auth and payments; integration plan once a choice is made | Five fixed query templates; fixed price and token tables that will age; no names step | MIT | 2025-12-31 | Plugin install | Web search |
| prior-art (bendrucker) | https://github.com/bendrucker/claude | GitHub, registries and web in parallel; reads 2–3 projects; honest about sparse results | Manual invocation only; no names, snowball or stop rule; nothing saved | MIT | 2026-11-12 (repo) | Part of a plugin | Web search |
| prior-work-retrieval (daymade) | https://github.com/daymade/claude-code-skills | The user's own history: code, documents, meetings, past conversations; receipts that separate retrieved, verified and reused; hooks that block writes until checked | External projects are out of scope by design | MIT | 2026-11-12 (repo) | Needs a source manifest and hook installation | Local files, shell hooks |
| research (MrToxy) | https://github.com/MrToxy/claude-skills | Four angles before a PRD: existing solutions, competitors, feasibility, own codebase; asks what was tried and abandoned; saves `docs/research/<name>.md` | General web search only; no names step; no stop rule | No licence file | 2026-08-21 | Copy one folder | Web search |
| librarian (roerohan) | https://github.com/roerohan/skills | Reading other people's code in depth: routes between code search, library docs and fetched source | Not a survey: assumes you know which library to read | MIT | 2026-09-04 | Needs three MCP tools | Network, MCP tools |
| code-search (athola) | https://github.com/athola/claude-night-market | GitHub search as one channel of a larger research plugin; reports an empty result explicitly | Depends on the plugin's Python helpers; one source | MIT | 2026-11-05 | Part of a plugin | Web search |
| idea-reality-mcp (mnemox-ai) | https://github.com/mnemox-ai/idea-reality-mcp | MCP tool; GitHub, HN, npm, PyPI, Product Hunt, Stack Overflow; one round of term expansion; 0–100 crowding score | The score counts repositories and stars, so it says how crowded a field is, not which project to use; nothing is opened and read; by default the idea text is posted to the author's hosted endpoint for keyword extraction (`scoring/llm.py`, `scoring/expansion.py`) | MIT | 2026-09-18 | `uvx idea-reality-mcp`. Only the scoring and source code were read. | Network; sends the idea text to a third-party server |
| AutoSearch (0xmariowu) | https://github.com/0xmariowu/autosearch | MCP search across 40 channels including 10+ Chinese-language sources | A search backend, not a survey procedure. Only the README was read. | MIT | 2026-06-01 | Python 3.12+ install. Not run. | Network |

## Seen, not read

Nothing here is a claim about what the project does beyond what a listing said.

| Project | Link | Where it came from |
|---|---|---|
| WheelSpotter (garylooop) | https://clawhub.ai/skills/wheelspotter | Name-check search. A third-party summary describes keyword extraction without expansion, star-threshold filtering, and found / not_found verdicts. The source was not reachable. |
| run-github-scout (yigitkonur) | https://github.com/yigitkonur/skills-by-yigitkonur | Round 3. A directory listing describes "alternatives to owner/repo" and a mode for fuzzy naming, which would overlap most with this skill. The skill was not in the repository on 2026-11-12. |
| GitHub Search & Discovery (majiayu000) | https://github.com/majiayu000/claude-skill-registry | Round 3, Chinese-language query. The path now holds only a pointer to an archived copy. |
| skill-hunter (mturac) | https://github.com/mturac/skill-hunter | Round 4. Could not be fetched on 2026-11-12. |
| github-prior-art (trevors) | https://github.com/trevors/dot-claude | Round 1. Could not be fetched on 2026-11-12. |
| github-prior-art-research (merceralex397-collab) | https://github.com/merceralex397-collab/Meta-Skill-Engineering | Round 1. Could not be fetched on 2026-11-12. |
| library-first-development (oisincoveney) | https://www.skills.sh/oisincoveney/skills/library-first-development | Round 4. Could not be fetched on 2026-11-12. |

## Ruled out

| Project | Reason |
|---|---|
| dont-reinvent, as a base to build on | Noncommercial licence. Its ideas are credited; none of its text is used. |
| research, as a base to build on | No licence file. |

## Name

The project was first drafted as "wheel-check" and renamed to 别重复造轮子
(`dont-reinvent-the-wheel`; GitHub repository names and skill names must be ASCII). The name
check found LucioLiu's `dont-reinvent` and gaupoit's "Don't Reinvent the Wheel" skill
(`programming-advisor`). Neither uses the exact slug, but the phrase is clearly taken as a
description, so expect confusion in search results.

## How it was searched

- Names tried: "prior art search", "existing solutions", "search first", "research before
  coding", "idea validation", "check existing projects", "wheel-check" and
  "dont-reinvent-the-wheel" (name checks), "避免重复造轮子", "已有项目调研", "find similar
  open source projects", "alternative".
- Sources searched: web search (7 queries); 12 repositories fetched and read.
- Sources that failed or were unavailable: the GitHub search API was not reachable from the
  environment this was written in, so `scout.py`'s `github` channel was **not exercised
  live**. ClawHub's page for WheelSpotter showed no content. Four repositories could not be
  fetched.
- Seeds snowballed from: none by script. Every round was new names, not README-following —
  which is how the first pass missed dont-reinvent until the name check found it.

## Not covered

- Gitee, Juejin and other Chinese-language sources beyond one web query.
- Skill directories searched directly (skills.sh, ClawHub, Tessl) instead of through web
  search.
- The seven projects under "Seen, not read".

The search stopped because the pattern was already clear: this field is crowded, and its
projects are hard to find because they share no name — "search-first", "prior-art",
"idea-check", "wheelspotter", "github-scout", "skill-scout", "dont-reinvent",
"programming-advisor", "skill-hunter". That is the problem this skill is about.
