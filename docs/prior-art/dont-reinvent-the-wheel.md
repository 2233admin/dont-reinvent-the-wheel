# Prior art: dont-reinvent-the-wheel（别重复造轮子）

- Date: 2026-11-12
- Mode: quick
- Searches used: 7 web searches, plus 6 repositories cloned and read
- Saturated: **no** — each of the four rounds added a project to the shortlist

This is the survey that was run before writing this skill, in the skill's own report format.

## Need

For a developer or coding agent about to build something: given a rough description of the
idea, find the existing projects that already do it, including ones described in different
words or another language, and end with a decision on whether to build.

Constraints: must work as a plain Agent Skill folder in any host that reads `SKILL.md`; no
required service, account or API key; permissive licence.

## Verdict

| Part | Verdict | Project | Why |
|---|---|---|---|
| Finding the user's own earlier work | Adopt (by reference) | prior-work-retrieval | Far more thorough than a step here could be. dont-reinvent-the-wheel keeps a light "look at home" step and points to it. |
| Fetching results from several sources | Compose | public registry and search APIs | A short standard-library script covers it. idea-reality-mcp and AutoSearch can be used as the first pass when installed. |
| Names, seed, snowball, stop rule | Build | — | See below. |
| Verdict rules and report | Extend (ideas) | search-first | Its verdict rules are stricter than ours. dont-reinvent-the-wheel uses a simpler table and recommends search-first when the decision needs rigour. |

**Build sentence.** Existing search-first cannot find a project the searcher has no name
for, because its steps go from stating the question to searching by question type: nothing
asks for the other names a thing goes by, and nothing follows a found project's own list of
alternatives. Its Full mode adds an "adversarial" angle that looks for other framings of the
problem, which is the closest it comes, and that mode relies on a `researcher` agent
definition and hooks from the author's own harness.

**How thin this is.** The new part is two steps and a state file. If search-first gained a
naming step and a snowball step, most of the reason for a separate skill would be gone. It
was kept separate because search-first's repository is published by a sync script from the
author's private harness (`scripts/sync-from-local.sh`), so changes to its flow may not be
accepted from outside. That is an inference, not something the author has said.

## Read

Cloned on 2026-11-12 and read in full unless noted.

| Project | Link | Covers | Lacks | Licence | Last commit | Cost to adopt |
|---|---|---|---|---|---|---|
| search-first (shimo4228) | https://github.com/shimo4228/search-first | Splits a plan into parts; checks the repo first; stop rule per question type; Adopt is the default and Build must name what rules each candidate out; report records terms searched and what was not found | No step for alternative names; no following of a project's listed alternatives; Full mode tied to the author's harness (ADR references, `researcher` agent, hooks) | MIT | 2026-11-01 | Copy one folder. Quick mode works anywhere. |
| prior-art (bendrucker) | https://github.com/bendrucker/claude | GitHub, registries and web in parallel; reads 2–3 projects; honest about sparse results | Manual invocation only (`disable-model-invocation: true`); no naming, snowball or stop rule; reports in chat, nothing saved | MIT | 2026-11-12 (repo) | Part of a plugin. |
| prior-work-retrieval (daymade) | https://github.com/daymade/claude-code-skills | The user's own history: code, documents, meetings, past conversations; receipts that separate retrieved, verified and reused; hooks that block writes until checked | External projects are out of scope by design | MIT | 2026-11-12 (repo) | Needs a source manifest and hook installation. |
| idea-reality-mcp (mnemox-ai) | https://github.com/mnemox-ai/idea-reality-mcp | MCP tool; GitHub, HN, npm, PyPI, Product Hunt, Stack Overflow; one round of term expansion (hosted LLM call, or an English synonym table as fallback); 0–100 crowding score | The score counts repositories and stars, so it says how crowded a field is, not which project to use; nothing is opened and read; by default the idea text is posted to the author's hosted endpoint for keyword extraction (`scoring/llm.py`, `scoring/expansion.py`) | MIT | 2026-09-18 | `uvx idea-reality-mcp`. Only the scoring and source code were read, not the whole repository. |
| AutoSearch (0xmariowu) | https://github.com/0xmariowu/autosearch | MCP search across 40 channels including 10+ Chinese-language sources | A search backend, not a survey procedure. Only the README was read. | MIT | 2026-06-01 | Python 3.12+ install. Not run. |

## Seen, not read

Found in skill directories or search snippets. Nothing here is a claim about what the project
does beyond what the listing said.

| Project | Link | Where it came from |
|---|---|---|
| WheelSpotter (garylooop) | https://clawhub.ai/skills/wheelspotter | Name-check search. A third-party summary describes keyword extraction without expansion, star-threshold filtering, and found / not_found verdicts. The source was not reachable. |
| run-github-scout (yigitkonur) | https://github.com/yigitkonur/skills-by-yigitkonur | Round 3. A directory listing describes "alternatives to owner/repo" and a mode for fuzzy naming, which would overlap most with dont-reinvent-the-wheel. The skill was not in the repository when cloned on 2026-11-12. |
| search-first (everything-claude-code) | https://github.com/affaan-m/everything-claude-code | Round 1. A different skill with the same name: npm/PyPI/MCP/GitHub checklist and a researcher agent. |
| skill-scout (everything-claude-code) | https://github.com/affaan-m/everything-claude-code | Round 3. Looks for existing skills before writing a new one. |
| GitHub Search & Discovery (majiayu000) | https://github.com/majiayu000/claude-skill-registry | Round 3, Chinese-language query. Written in Chinese. |
| github-prior-art (trevors) | https://github.com/trevors/dot-claude | Round 1. |
| github-prior-art-research (merceralex397-collab) | https://github.com/merceralex397-collab/Meta-Skill-Engineering | Round 1. Listing mentions licence data and adopt / adapt / build. |
| code-search (athola) | https://github.com/athola/claude-night-market | Round 1. |
| research (MrToxy) | https://github.com/MrToxy/claude-skills | Round 1. Pre-PRD research in four dimensions. |
| dont-reinvent (LucioLiu) | https://huggingface.co/datasets/LucioLiu/dont-reinvent | Round 4, the name check for this project. Its page describes finding existing *skills* before building one, from a fixed list of skill sources; English and Chinese. The closest name to ours. |
| programming-advisor (gaupoit) | https://github.com/gaupoit/programming-advisor | Round 4. Its author calls it a "Don't Reinvent the Wheel" skill; triggers on "I want to build a…". |
| skill-hunter (mturac) | https://github.com/mturac/skill-hunter | Round 4. Checks for an existing skill before the agent writes one. |
| library-first-development (oisincoveney) | https://www.skills.sh/oisincoveney/skills/library-first-development | Round 4. |
| librarian (roerohan) | https://github.com/roerohan/skills | Round 4. Researches library internals across GitHub and registries. |

## Ruled out

None on licence or maintenance grounds. Every project read is MIT-licensed.

## How it was searched

- Names tried: "prior art search", "existing solutions", "search first", "research before
  coding", "idea validation", "check existing projects", "wheel-check" and "dont-reinvent-the-wheel" (name checks),
  "避免重复造轮子", "已有项目调研", "find similar open source projects", "alternative".
- Sources searched: web search (7 queries); six GitHub repositories cloned and read.
- Sources that failed or were unavailable: the GitHub search API was not reachable from the
  environment this was written in, so `scout.py`'s `github` channel was **not exercised
  live**. ClawHub's page for WheelSpotter showed no content.
- Seeds snowballed from: none by script. The second and third rounds were new names, not
  README-following.

## Name

The project was first drafted as "wheel-check" and renamed to 别重复造轮子
(`dont-reinvent-the-wheel`; GitHub repository names and skill names must be ASCII). The name
check found LucioLiu's `dont-reinvent` and gaupoit's "Don't Reinvent the Wheel" skill
(`programming-advisor`). Neither uses the exact slug, but the phrase is clearly taken as a
description, so expect confusion in search results.

## Not covered

- Gitee, Juejin and other Chinese-language sources beyond one web query.
- Skill directories searched directly (skills.sh, ClawHub, Tessl) instead of through web
  search.
- The fourteen projects under "Seen, not read".
- Whether run-github-scout still exists under another name.

The search stopped because the pattern was already clear: this field is crowded, and its
projects are hard to find because they share no name — "search-first", "prior-art",
"idea-check", "wheelspotter", "github-scout", "skill-scout", "dont-reinvent",
"programming-advisor", "skill-hunter". That is the problem
this skill is about.
