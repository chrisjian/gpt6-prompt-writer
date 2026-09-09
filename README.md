# 多模型提示词工程 Skill

把模糊需求写成不同前沿模型都能执行、检查和交付的高质量提示词，并把**通用 Prompt Engineering Core**与**模型特有 Profile**分开维护。

当前已核验 Profile：

- GPT‑6 Astra
- Claude Fable 5
- Claude Fable 5.1
- Grok 4.6

仓库名暂时仍为 `gpt6-prompt-writer`，但 Skill 本身已重构为 `multi-model-prompt-writer`。后续如需，可再单独重命名 GitHub 仓库；不影响当前分支内容。

## 设计目标

本 Skill 不再以 GPT‑6 为中心再“兼容其他模型”，而采用平级结构：

```text
Universal Prompt Engineering Core
            │
            ├── GPT-6 Astra Profile
            ├── Claude Fable 5 Profile
            ├── Claude Fable 5.1 Profile
            └── Grok 4.6 Profile
```

Core 只放跨模型成立的工程原则；模型默认 effort、格式倾向、验证倾向、搜索行为、API 字段和 migration workaround 必须下沉到对应 Profile。

## 显式调用

这个 Skill 体量较大，默认**不自动进入上下文**：

- Claude Code 风格：`disable-model-invocation: true`
- OpenAI/Codex 风格：`policy.allow_implicit_invocation: false`

显式调用示例：

```text
$multi-model-prompt-writer 把这段旧 prompt 优化给 GPT-6 Astra 用，保留行为约束但删掉旧模型 workaround：……
```

```text
$multi-model-prompt-writer 给 Claude Fable 5.1 写一个长任务 Agent prompt，重点控制范围、完成状态和最终汇报可读性。
```

```text
$multi-model-prompt-writer 给 Grok 4.6 写研究 prompt；如果需要今天的信息，要求使用实际启用的 Web Search / X Search。
```

## 核心能力

- **最小任务契约**：目标、输入、受众、必要用途、硬约束、交付物、完成标准、缺失处理。
- **可观察验收**：把“专业、深入、高质量”转成可检查结果。
- **根因级指令**：一个高层行为原则优先于一串症状级禁令。
- **Prompt Audit**：删除重复、冲突、模糊强化、旧模型 workaround 和无目的流程。
- **行为保真压缩**：减少 instruction surface area，但保留事实、权限、格式和失败分支等不变量。
- **意图边界**：区分 analysis / advice / action，避免既擅自执行也避免明确行动请求被降级成能力说明。
- **状态真实性**：计划、推断和意图不能冒充已搜索、已验证、已完成；证据默认按需披露，避免输出膨胀。
- **可读性简洁**：通过删除低价值信息变短，不靠电报体、箭头链和术语堆积。
- **代表性正例**：微妙行为在规则仍不稳定时，用一个短正例替代继续堆禁令。
- **模型适配层**：只加入对应厂商官方文档或可复现实测支持的特例。

## 文件结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── core/
│   │   ├── prompt-principles.md
│   │   └── prompt-patterns.md
│   └── models/
│       ├── gpt-6-astra.md
│       ├── claude-fable-5.md
│       ├── claude-fable-5.1.md
│       └── grok-4.6.md
├── evals/
│   ├── core.json
│   └── models/
│       ├── gpt-6-astra.json
│       ├── claude-fable-5.json
│       ├── claude-fable-5.1.json
│       └── grok-4.6.json
├── examples/
│   ├── worked-examples.md
│   └── extraction-request.json
└── scripts/
    └── validate.py
```

## 使用逻辑

```text
用户需求 / 旧 Prompt
        ↓
识别目标模型（若有）
        ↓
Universal Core
        ↓
目标模型 Profile
        ↓
宿主 / API 真实能力核验
        ↓
最终 Prompt
        ↓
Core + Profile Evals
```

如果用户没指定模型，默认只使用 Core。只有模型差异会实质改变结果时，才需要知道目标模型；不要为了形式完整强制先问模型。

## 模型 Profile 原则

每个 Profile 都必须包含：

- Official sources
- Verified model behaviors / facts
- Prompt adaptations
- API / runtime notes
- Migration notes（若相关）
- **Do not generalize**

最后一项用于防止某个模型的 workaround 再次污染 Core。

### GPT‑6 Astra

当前依据 OpenAI 官方 Model Guidance 和 Model Page，记录 initiative、Skill/AGENTS 敏感度、格式倾向、delegation、验证倾向，以及 `gpt-6-astra`、reasoning、Responses/tool calling、Structured Outputs 等 API 事实。

### Claude Fable 5 / 5.1

当前依据 Anthropic 官方 Prompting Guide 与 Claude prompting best practices。Fable 5 与 5.1 分开维护，因为 effort、搜索触发、写作密度、格式、文件编辑、history/runtime 等行为存在版本差异。

### Grok 4.6

当前依据 xAI 官方 Grok 4.6、Models、Prompt Caching、Context Compaction 和 Grok Build 文档。xAI 当前可核验的模型/API 事实较充分，但没有发现与 OpenAI/Anthropic 同等级的通用文本模型 Prompting Guide，因此 Profile **不会凭经验写入 Markdown、测试、delegation、clarification 等行为倾向**；这些需要官方证据或可重复 eval 后再加入。

## Evals

回归测试分两层：

- `evals/core.json`：跨模型原则。
- `evals/models/*.json`：模型特有行为/API 适配。

这允许比较：

```text
Core only
vs
Core + target model profile
```

并能避免“某个模型的测试通过”被误当成通用 Prompt 原则。

当前这些文件仍是**测试输入与判定标准**，不是模型实际通过记录。需要真实回放时应记录模型版本、日期、effort/reasoning、Skill commit、输入、输出和判定结果。

## 静态校验

```bash
python3 scripts/validate.py
```

静态检查包括：Skill metadata、显式调用策略、必需文件、Profile 结构、Markdown 相对引用、JSON eval 格式与跨文件 case ID 唯一性。它不调用模型，不代表真实 Prompt 效果已经验证。

## 安装当前开发分支

当前多模型重构位于 fork 的 `prompt-quality-v1.1`：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo chrisjian/gpt6-prompt-writer \
  --ref prompt-quality-v1.1 \
  --path . \
  --name multi-model-prompt-writer
```

安装后显式使用 `$multi-model-prompt-writer`。

## 依据与维护

当前模型资料核验日期：**2026-09-09**。

主要官方入口：

- OpenAI GPT‑6 Astra: https://developers.openai.com/api/docs/guides/latest-model
- Anthropic Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic Fable 5: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- Anthropic Fable 5.1: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
- xAI Grok 4.6: https://docs.x.ai/developers/grok-4-6

要求“最新/官方”或可运行 API 配置时，应重新打开对应厂商文档，而不是把仓库快照当永久事实。
