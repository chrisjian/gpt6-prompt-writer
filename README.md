# 多模型提示词工程 Skill

把模糊需求写成不同前沿模型都能执行、检查和交付的高质量提示词，并把**通用 Prompt Engineering Core**与**模型家族 Profile**分开维护。

仓库名与 Skill 名统一为 `multi-model-prompt-writer`。

## 当前 Profile

| 厂商 | Profile | 粒度 |
| --- | --- | --- |
| OpenAI | GPT‑6 Astra | model |
| OpenAI | GPT‑5.6 | family：Sol / Terra / Luna variants |
| Anthropic | Claude Fable 5 | model |
| Anthropic | Claude Fable 5.1 | model |
| Google | Gemini 3.x | family |
| xAI | Grok 4.6 | model |
| DeepSeek | DeepSeek V4 | family：Pro / Flash variants |
| 智谱 | GLM 5.x | family：5 / 5.1 / 5.2 versions |
| 火山引擎 | Doubao Seed 2.x | thin family：Pro / Lite / Mini / Code |

Profile 不是“支持列表越长越好”。只有模型家族存在足以改变 Prompt 或 runtime 设计的差异时才建立；variant 优先写成 family 内差异，不复制整套方法论。

## 架构

```text
Universal Prompt Engineering Core
            │
            ├── OpenAI
            │   ├── GPT-6 Astra
            │   └── GPT-5.6 → Sol / Terra / Luna
            ├── Anthropic
            │   ├── Claude Fable 5
            │   └── Claude Fable 5.1
            ├── Google → Gemini 3.x
            ├── xAI → Grok 4.6
            ├── DeepSeek → V4 Pro / Flash
            ├── Zhipu → GLM 5.x
            └── Volcengine → Doubao Seed 2.x
```

Core 只放跨模型成立的工程原则；默认 effort、格式倾向、搜索行为、reasoning state、API 字段和 migration workaround 必须下沉到对应 Profile。

## 显式调用

这个 Skill 体量较大，默认**不自动进入上下文**：

- Claude Code 风格：`disable-model-invocation: true`
- OpenAI/Codex 风格：`policy.allow_implicit_invocation: false`

示例：

```text
$multi-model-prompt-writer 把这段旧 prompt 优化给 Gemini 3 用，删掉旧式 step-by-step forcing：……
```

```text
$multi-model-prompt-writer 给 DeepSeek V4 Pro 写一个 thinking + tools Agent prompt，并把 runtime 接入要求和模型可见提示词分开。
```

```text
$multi-model-prompt-writer 给 GPT-5.6 Luna 写批量摘要 prompt，保持事实边界，不因为成本优先而降低验收标准。
```

## 核心能力

- **最小任务契约**：目标、输入、受众、必要用途、硬约束、交付物、完成标准、缺失处理。
- **可观察验收**：把“专业、深入、高质量”转成可检查结果。
- **根因级指令**：一个高层行为原则优先于一串症状级禁令。
- **Prompt Audit**：删除重复、冲突、模糊强化、旧模型 workaround 和无目的流程。
- **行为保真压缩**：减少 instruction surface area，但保留事实、权限、格式和失败分支等不变量。
- **意图边界**：区分 analysis / advice / action。
- **状态真实性**：计划、推断和意图不能冒充已搜索、已验证、已完成；证据默认按需披露。
- **可读性简洁**：通过删除低价值信息变短，不靠电报体、箭头链和术语堆积。
- **代表性正例**：微妙行为在规则仍不稳定时，用一个短正例替代继续堆禁令。
- **模型适配层**：只加入对应厂商官方文档或可复现实测支持的特例。

## 文件结构

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── core/
│   │   ├── prompt-principles.md
│   │   └── prompt-patterns.md
│   └── models/
│       ├── openai/
│       │   ├── gpt-6-astra.md
│       │   └── gpt-5.6.md
│       ├── anthropic/
│       │   ├── claude-fable-5.md
│       │   └── claude-fable-5.1.md
│       ├── google/gemini-3.x.md
│       ├── xai/grok-4.6.md
│       ├── deepseek/deepseek-v4.md
│       ├── zhipu/glm-5.x.md
│       └── volcengine/doubao-seed-2.x.md
├── evals/
│   ├── core.json
│   └── models/<vendor>/*.json
├── examples/
│   ├── worked-examples.md
│   └── extraction-request.json
└── scripts/validate.py
```

## 使用逻辑

```text
用户需求 / 旧 Prompt
        ↓
识别目标模型或 family（若有）
        ↓
Universal Core
        ↓
Family / Model Profile
        ↓
Variant notes（仅必要差异）
        ↓
宿主 / API 真实能力核验
        ↓
最终 Prompt
        ↓
Core + Profile Evals
```

如果用户没指定模型，默认只使用 Core。只有模型差异会实质改变结果时，才需要知道目标模型；不要为了形式完整强制先问模型。

## Profile 设计规则

每份 Profile 至少包含：

- Official sources
- Verified model behaviors / facts
- Prompt adaptations
- API / runtime notes
- Variant / migration notes（若相关）
- **Do not generalize**

最后一项用于防止某个模型的 workaround 再次污染 Core。

### GPT‑5.6

Sol / Terra / Luna 共用 family Profile。当前官方差异主要是能力、吞吐和成本定位；没有足够依据时不为三个 SKU 复制不同的 Prompt 方法论。

### Gemini 3.x

依据 Google 官方 Gemini 3 指南维护 `thinking_level`、默认 temperature、thought signatures、旧式 CoT forcing 迁移和长上下文提示结构。

### DeepSeek V4

依据官方 V4 thinking/API 文档维护默认 thinking、effort 映射、thinking 模式 sampling 参数失效，以及 tools 场景 `reasoning_content` state。

### GLM 5.x

按版本区分 context、thinking、`reasoning_effort` 和 interleaved thinking。GLM‑5.2 的 1M context 与 reasoning 参数不能反向套给 GLM‑5。

### Doubao Seed 2.x

当前保持 thin Profile：记录 Pro/Lite/Mini/Code 定位、thinking/runtime 与 Coding Plan/在线推理边界；没有高质量官方文本 Prompting Guide 时不臆造 Markdown、verbosity、testing 等行为倾向。

## Evals

回归测试分两层：

- `evals/core.json`：跨模型原则。
- `evals/models/<vendor>/*.json`：模型/family 特有行为与 API 适配。

这些文件是**测试输入与判定标准**，不是模型实际通过记录。真实回放应记录模型版本、日期、effort/reasoning、Skill commit、输入、输出和判定结果。

## 静态校验

```bash
python3 scripts/validate.py
```

静态检查包括 Skill metadata、显式调用策略、厂商目录、Profile 结构、Markdown 相对引用、JSON eval 格式、case ID 唯一性，以及 GPT‑6 示例请求契约。它不调用模型，不代表 Prompt 效果已经验证。

## 安装当前开发分支

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo chrisjian/multi-model-prompt-writer \
  --ref prompt-quality-v1.1 \
  --path . \
  --name multi-model-prompt-writer
```

安装后显式使用 `$multi-model-prompt-writer`。

## 依据与维护

当前模型资料核验日期：**2026-09-09**。

主要官方入口：

- OpenAI: https://developers.openai.com/api/docs/models
- Anthropic: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Google Gemini 3: https://ai.google.dev/gemini-api/docs/gemini-3
- xAI Grok 4.6: https://docs.x.ai/developers/grok-4-6
- DeepSeek V4: https://api-docs.deepseek.com/guides/thinking_mode/
- GLM: https://docs.bigmodel.cn/cn/guide/models/text/glm-5.2
- Doubao/Volcengine: https://developer.volcengine.com/articles/7610285824933445675

要求“最新/官方”或可运行 API 配置时，应重新打开对应厂商文档，而不是把仓库快照当永久事实。
