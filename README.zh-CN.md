# 别重复造轮子

[English](README.md)

<p align="center">
  <img src="docs/assets/banner.svg" width="840" alt="黑白 ASCII 巨构建筑：用字符画出的无尽立柱、桁架和管道。一个戴琥珀色安全帽的像素小人沿着栈桥往前走，打算造一个轮子，然后停在一个一直在那里转动的巨型轮子面前。字幕：它早就在这里了。结论：直接用。">
</p>

一个 agent skill，用在你正要动手造东西的时候。它把已经有的找出来，包括那些因为不知道叫什么而永远搜不到的。

```text
 need -> name it 6 ways -> find a seed -> snowball -> quiet? -yes-> read <=5 -> verdict -> report
              ^                                         |
              +------------------- no ------------------+

 需求 -> 换六种叫法 -> 找一个种子 -> 滚雪球 -> 安静了吗 -是-> 精读最多五个 -> 结论 -> 报告
```

## 问题在哪

“动手前先搜一下 GitHub”经常搜不到，原因通常只有一个：东西是有的，但名字和你搜的词不一样。

我们给这个 skill 自己做调查时就遇到了。同一个想法，别人分别叫 `search-first`、`prior-art`、`idea-check`、`wheelspotter`、`github-scout`、`skill-scout`、`dont-reinvent`、`programming-advisor`、`skill-hunter`。没有哪个关键词能一次搜全，我们搜了四轮才陆续找到。

## 它做什么

1. **先换词，再搜。** 行业术语、用户原话、另一种语言、所属类别、已知的同类产品、“现成项目的 README 第一句话大概怎么写”，以及没有这个工具时人们怎么抱怨。
2. **找一个种子，再滚雪球。** 读种子项目自己写的 Alternatives、它的 topics、它所在的 awesome 列表。作者比搜索引擎更清楚自己的竞品。
3. **搜索安静下来就停。** 连续两轮没有新项目进入候选名单就停。脚本负责计数，“搜够了”是一个数字。
4. **先读，再下结论。** 最多精读五个：README、一个核心源文件、issue 区、它要哪些权限、以后怎么更新。
5. **留一份带日期的报告。** 写到 `docs/prior-art/`，记下用过的词和来源，下次查同一个题目从这里接着查。

第 2、3 步是我们自己做的。其余部分是从别的 skill 借来的想法，见[借鉴来源](#借鉴来源)。

## 你会得到什么

需求的每个部分一个结论。下面是[这个 skill 给自己做的调查](docs/prior-art/dont-reinvent-the-wheel.md)里的真实结果：

| 部分 | 结论 | 项目 |
|---|---|---|
| 找用户自己以前做过的东西 | Adopt（指过去） | prior-work-retrieval |
| 从多个来源取结果 | Compose | 各家公开的搜索接口 |
| 调查力度、换词、筛选、结论规则 | Extend（借想法） | search-first、dont-reinvent、skill-scout、programming-advisor |
| 种子、滚雪球、停止规则、带日期的报告 | Build | — |

结论有五种：**Adopt（直接用）、Extend（在它上面改）、Compose（拼起来）、Build（自己造）、Keep（保留现有的）**。要给 Build，必须写得出这句话：“现有的 X 做不到 ___，因为 ___。”“为了学习”“为了好玩”也是正当理由，照实写成理由就行。

## 和原型同时进行，不是先调查再动手

调查不是门槛。现在动手很便宜，粗糙原型可以马上开做，调查同时跑。原型做的过程中碰到的术语、库名、报错，正好拿回来当搜索词。调查只需要赶在“停下来变贵”之前做完：别人开始依赖它之前、投入一周之前、对外宣布之前。

## 安装

skill 本体是 `skills/dont-reinvent-the-wheel` 这个文件夹，复制到你的 agent 的 skills 目录即可：

```bash
git clone https://github.com/2233admin/dont-reinvent-the-wheel
cp -r dont-reinvent-the-wheel/skills/dont-reinvent-the-wheel ~/.claude/skills/   # Claude Code
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

也可以自己跑脚本：

```bash
cd skills/dont-reinvent-the-wheel
S=.prior-art/link-checker.json

python3 scripts/scout.py check                                  # 哪些来源连得上
python3 scripts/scout.py search  --state $S -t "markdown link checker" \
        -t "dead link checker" -t "死链检查" --channels github,hn,npm
python3 scripts/scout.py keep    --state $S lycheeverse/lychee  # 值得细看的记下来
python3 scripts/scout.py related --state $S lycheeverse/lychee  # 它的 README 提到了谁
python3 scripts/scout.py status  --state $S                     # 搜索安静了没有
```

| 命令 | 作用 |
|---|---|
| `check` | 每个来源发一个最小请求，告诉你哪些能用 |
| `search` | 把每个词发给每个来源，合并结果；被多个词同时命中的排在前面 |
| `keep` | 把候选记进名单 |
| `related` | 列出种子项目 README 里提到的其他项目，Alternatives 一类章节下的排最前 |
| `status` | 已经搜了几轮、名单里有谁、名单是否连续两轮没变 |

star 和下载量只显示，不参与排序。某个来源请求失败时，会明确写“没有搜到这个来源”，不会当成“没有结果”。设置 `GITHUB_TOKEN` 可以提高 GitHub 搜索的频率上限。

## 借鉴来源

一个叫“别重复造轮子”的 skill 如果是从零写的，就太没有说服力了。初稿写完后我们通读了十二个同类项目，把它们做得更好的地方拿了过来。只借想法，没有复制任何文字。

| 想法 | 来自 |
|---|---|
| 把需求拆成零件；Build 要自己举证；说清楚每个候选为什么不行；记录搜过的词 | [search-first](https://github.com/shimo4228/search-first) |
| 调查力度和风险相称；除了名字还要搜“抱怨”；用户点名的候选也要再看两个邻居；Keep 结论；记录来源、版本和更新方式；检查候选要哪些权限 | [dont-reinvent](https://github.com/LucioLiu/dont-reinvent) |
| 先确认哪些来源连得上；Compose 结论 | everything-claude-code 里的 [search-first](https://github.com/affaan-m/everything-claude-code) |
| 按描述搜已安装的 skill；推荐一个 skill 之前先读它会执行什么命令 | [skill-scout](https://github.com/affaan-m/everything-claude-code) |
| 托管服务也算候选；认证、加密、支付这几类自己造的门槛更高 | [programming-advisor](https://github.com/gaupoit/programming-advisor) |
| 来源失败不等于没有结果；“读过”和“见过”是两种说法 | [prior-work-retrieval](https://github.com/daymade/claude-code-skills) |
| 找到的少就照实说少；只出结论，不替用户动手 | [prior-art](https://github.com/bendrucker/claude) |
| 弃坑的项目要问一句为什么停了 | [research](https://github.com/MrToxy/claude-skills) |
| 要找的是一段写法而不是一个项目时该去哪搜 | [librarian](https://github.com/roerohan/skills) |
| 多个来源并行查 | [idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp) |

## 同类项目

下面几个项目各有这个 skill 没有的东西。细节和日期见[调查报告](docs/prior-art/dont-reinvent-the-wheel.md)。

| 项目 | 什么时候该用它 |
|---|---|
| [search-first](https://github.com/shimo4228/search-first) | 已经知道该搜什么，需要一个严格的“用现成的还是自己造”的决定。它的判定规则比我们严。两者可以配合：这个 skill 负责找，search-first 负责定。 |
| [dont-reinvent](https://github.com/LucioLiu/dont-reinvent) | 你要做的东西本身是一个 skill 或团队里可复用的能力，而且希望装完之后有登记、能更新。注意它是非商业许可证。 |
| [prior-work-retrieval](https://github.com/daymade/claude-code-skills) | 问题是“我们自己以前做过没有”：自己的代码、文档、历史对话。 |
| [programming-advisor](https://github.com/gaupoit/programming-advisor) | 想要一份“自己造还是买现成的”成本对比，以及选定之后的接入步骤。 |
| [idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp) | 想快速得到一个“这个想法有多挤”的分数。也可以当这个 skill 的第一轮搜索。 |
| [AutoSearch](https://github.com/0xmariowu/autosearch) | 需要覆盖很多来源，包括中文来源。它是搜索后端，这个 skill 可以架在它上面。 |

## 局限

- 目前是 0.1 版。还没有 agent 拿它完整查过一个真题目，也没有和“不用它”的情况做过对比。
- `github` 这个来源还没有对着真实接口跑过，另外四个跑过。
- 停止规则要靠 agent 自己标记哪些值得保留。脚本只计数，不判断相关性。
- PyPI 没有搜索接口。`pypi` 这个来源只能检查有没有以该词命名的包。
- 包管理器不擅长按概念搜索，只适合找库。
- 这里真正新的东西不多：滚雪球那一步和停止计数。上面哪个项目要是加上了这两样，就用它。

## 开发

```bash
python3 -m unittest discover -s tests
```

## 许可证

MIT
