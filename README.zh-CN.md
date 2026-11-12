# 别重复造轮子

[English](README.md)

<p align="center">
  <img src="docs/assets/banner.svg" width="840" alt="黑白 ASCII 巨构建筑：用字符画出的无尽立柱、桁架和管道。一个戴琥珀色安全帽的像素小人沿着栈桥往前走，打算造一个轮子，然后停在一个一直在那里转动的巨型轮子面前。字幕：它早就在这里了。结论：直接用。">
</p>

一个 agent skill：动手造之前，先把已经有的找出来。重点解决“不知道现成的东西叫什么”的情况。

## 为什么要有它

“动手前先搜一下 GitHub”听起来简单，实际经常搜不到。原因通常只有一个：东西是有的，但名字和你搜的词不一样。

我们给这个 skill 自己做已有工作调查时就遇到了。同一个想法，别人分别叫 `search-first`、`prior-art`、`idea-check`、`wheelspotter`、`github-scout`、`skill-scout`。没有哪个关键词能把它们一次搜全。

所以 dont-reinvent-the-wheel 把力气花在这四件事上：

1. **先换词，再搜**。每个需求写出六种叫法：行业术语、用户原话、另一种语言、所属类别、已知的同类产品、以及“现成项目的 README 第一句话大概会怎么写”。
2. **找一个种子，再滚雪球**。读种子项目自己写的 Alternatives、它的 topics、它所在的 awesome 列表。作者比搜索引擎更清楚自己的竞品。
3. **搜索安静下来就停**。连续两轮没有新项目进入候选名单，就停。脚本负责计数，“搜够了”是一个数字。
4. **留一份带日期的报告**。写到 `docs/prior-art/`，记下用过的词和来源。下次查同一个题目，从这份报告接着查。

调查不是门槛。它应该和第一个粗糙原型同时进行：原型做出来的过程中碰到的术语、库名、报错，正好拿回来当搜索词。

最后对需求的每个部分给出四种结论之一：**Adopt（直接用）、Extend（在它上面改）、Compose（拼起来）、Build（自己造）**。要给 Build，必须写得出这句话：“现有的 X 做不到 ___，因为 ___。”

## 安装

skill 本体是 `skills/dont-reinvent-the-wheel` 这个文件夹，复制到你的 agent 的 skills 目录即可：

```bash
git clone https://github.com/2233admin/dont-reinvent-the-wheel
cp -r dont-reinvent-the-wheel/skills/dont-reinvent-the-wheel ~/.claude/skills/        # Claude Code
```

或者用 `skills` 命令行：

```bash
npx skills add 2233admin/dont-reinvent-the-wheel
```

需要 agent 能联网搜索，或者 shell 能访问网络。自带脚本只需要 Python 3.8+，没有其他依赖。

## 使用

照平时的说法问就行：

> 我想做个从 AI 平台抓提示词和封面的素材库插件，先查查有没有现成的。
>
> 别重复造轮子，调研一下已有的。

也可以直接用脚本：

```bash
S=.prior-art/link-checker.json
python3 skills/dont-reinvent-the-wheel/scripts/scout.py search --state $S \
  -t "markdown link checker" -t "dead link checker" -t "死链检查" --channels github,hn,npm
python3 skills/dont-reinvent-the-wheel/scripts/scout.py keep    --state $S lycheeverse/lychee
python3 skills/dont-reinvent-the-wheel/scripts/scout.py related --state $S lycheeverse/lychee
python3 skills/dont-reinvent-the-wheel/scripts/scout.py status  --state $S
```

- `search`：把每个词发给每个来源，合并结果。被多个词同时命中的排在前面。
- `keep`：把值得细看的项目记进候选名单。
- `related`：列出种子项目 README 里提到的其他项目。
- `status`：告诉你搜索是不是已经安静了。

star 和下载量只显示，不参与排序。某个来源请求失败时，会明确写“没有搜到这个来源”，不会当成“没有结果”。

设置 `GITHUB_TOKEN` 可以提高 GitHub 搜索的频率上限。

## 局限

- 停止规则要靠 agent 自己标记哪些值得保留。脚本只计数，不判断相关性。
- PyPI 没有搜索接口。`pypi` 这个来源只能检查有没有以该词命名的包。
- 包管理器不擅长按概念搜索，只适合找库。
- 这个 skill 还没有和“不用 skill”的情况做过对比测试；首次提交时，`github` 来源还没有对着真实接口跑过。详见[调查报告](docs/prior-art/dont-reinvent-the-wheel.md)。

## 同类项目

这个方向已经很挤，下面几个项目各有 dont-reinvent-the-wheel 没有的东西。细节和日期见 [docs/prior-art/dont-reinvent-the-wheel.md](docs/prior-art/dont-reinvent-the-wheel.md)。

| 项目 | 什么时候该用它 |
|---|---|
| [search-first](https://github.com/shimo4228/search-first) | 已经知道该搜什么，需要一个严格的“用现成的还是自己造”的决定。它的判定规则比我们严。两者可以配合：dont-reinvent-the-wheel 负责找，search-first 负责定。 |
| [prior-work-retrieval](https://github.com/daymade/claude-code-skills) | 问题是“我们自己以前做过没有”：自己的代码、文档、历史对话。 |
| [idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp) | 想快速得到一个“这个想法有多挤”的分数。也可以当 dont-reinvent-the-wheel 的第一轮搜索。 |
| [AutoSearch](https://github.com/0xmariowu/autosearch) | 需要覆盖很多来源，包括中文来源。它是搜索后端，dont-reinvent-the-wheel 可以架在它上面。 |
| [prior-art](https://github.com/bendrucker/claude) | 只想要一个手动命令，在对话里总结几个项目。 |

另外有一个名字很像的 [dont-reinvent](https://huggingface.co/datasets/LucioLiu/dont-reinvent)，它管的是“写新 skill 之前先找现成的 skill”，不是同一个项目。

## 开发

```bash
python3 -m unittest discover -s tests
```

## 许可证

MIT
