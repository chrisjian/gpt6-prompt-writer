# 多模型提示词工程 Skill

面向日常工作与 coding-agent 场景，把模糊需求写成不同前沿模型可以执行、检查和交付的高质量 Prompt。仓库名与 Skill 名均为 `multi-model-prompt-writer`。

核心设计是把三类知识严格分开：

```text
Core    = 跨模型 Prompt Engineering 方法
Models  = 会直接改变自然语言 Prompt 写法的模型行为
API     = 程序化参数、协议、状态与接入细节（默认冷加载）
```

Harness（Codex、Claude Code、Cursor、Grok Build 等）的 rules / skills / subagents / hooks / permissions 等机制现阶段不建立长期 Profile；只有任务确实依赖这些机制时才实时核验当前官方行为。

## 当前 Model Profiles

| 厂商 | Profile | 粒度 |
| --- | --- | --- |
| OpenAI | GPT‑6 Astra | model |
| OpenAI | GPT‑5.6 | family：Sol / Terra / Luna |
| Anthropic | Claude Fable 5 | model |
| Anthropic | Claude Fable 5.1 | model |
| Google | Gemini 3.x | family |
| xAI | Grok 4.6 | model |
| DeepSeek | DeepSeek V4 | family：Pro / Flash |
| 智谱 | GLM 5.x | family |
| 火山引擎 | Doubao Seed 2.x | thin family：Pro / Lite / Mini / Code |

Profile 不是支持列表越长越好。只有某个模型/家族存在足以改变 Prompt 设计的差异时才建立；API 参数差异不构成独立 Prompt 方法论。

## 默认加载策略

普通 Prompt、coding-agent Prompt、研究/写作 Prompt、Prompt 审计与压缩：

```text
Universal Core
      +
Target Model Profile（若模型明确）
      ↓
Final Prompt
```

只有用户明确要求以下内容时才加载 `references/api/`：

- API / SDK / request body
- model ID / endpoint
- reasoning / effort / thinking 参数
- context / max output
- Structured Outputs / JSON 配置
- tool-calling protocol
- conversation / reasoning state
- cache / compaction
- 程序化接口迁移

即使用户说“给 GPT‑6 / DeepSeek / Gemini 写 coding prompt”，也**不会仅因为模型明确就加载 API reference**。

## 显式调用

Skill 体量较大，默认不自动进入上下文：

- Claude Code 风格：`disable-model-invocation: true`
- OpenAI/Codex 风格：`policy.allow_implicit_invocation: false`

示例：

```text
$multi-model-prompt-writer 把这段 coding prompt 优化给 GPT-6 Astra 用，减少无意义确认和过度测试：……
```

```text
$multi-model-prompt-writer 把 Gemini 2.5 的旧 prompt 迁到 Gemini 3，删除不再必要的 step-by-step forcing：……
```

只有明确 API 请求才进入冷资料层：

```text
$multi-model-prompt-writer 给 DeepSeek V4 Pro 写 thinking + tools 的 API 接入要求，并把 API state 和模型可见 Prompt 分开。
```

## 核心能力

- **最小任务契约**：目标、输入、受众、必要用途、硬约束、交付物、完成标准、缺失处理。
- **可观察验收**：把“专业、深入、高质量”转成可检查结果。
- **根因级指令**：一个高层行为原则优先于一串症状级禁令。
- **Prompt Audit**：删除重复、冲突、模糊强化、旧模型 workaround 和无目的流程。
- **行为保真压缩**：减少 instruction surface area，同时保留事实、权限、格式和失败分支等不变量。
- **状态真实性**：计划、推断和意图不能冒充已搜索、已验证、已完成。
- **模型适配**：只加入有官方依据或可复现实测支持、且确实改变 Prompt 写法的特例。
- **API 冷加载**：参数/协议不再污染普通 Model Profile 和日常 Prompt 上下文。

## 文件结构

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── core/
│   │   ├── prompt-principles.md
│   │   └── prompt-patterns.md
│   ├── models/
│   │   ├── openai/
│   │   ├── anthropic/
│   │   ├── google/
│   │   ├── xai/
│   │   ├── deepseek/
│   │   ├── zhipu/
│   │   └── volcengine/
│   └── api/
│       ├── openai.md
│       ├── anthropic.md
│       ├── google.md
│       ├── xai.md
│       ├── deepseek.md
│       ├── zhipu.md
│       └── volcengine.md
├── evals/
│   ├── core.json
│   ├── models/<vendor>/*.json
│   └── api/*.json
├── examples/
│   ├── worked-examples.md
│   └── api/openai-extraction-request.json
└── scripts/validate.py
```

## 分层判断规则

### 放进 Model Profile

如果删除这条信息，会让最终生成的**自然语言 Prompt**明显变差或写错，例如：

- GPT‑6 Astra 容易过度验证或过度格式化；
- Fable 5.1 low effort 下当前事实任务可能需要更明确的搜索触发；
- Gemini 3 迁移时应删除旧式 CoT forcing，并注意长上下文任务布局；
- 某模型/版本存在稳定的 scope、editing、delegation 等 Prompt 行为差异。

### 放进 API Reference

如果它主要决定“调用模型的代码怎么写”，例如：

- model ID / alias
- effort / thinking / sampling 参数
- context / max output
- Responses / Chat 等接口
- `reasoning_content` / thought signatures
- Structured Outputs / JSON Output
- cache / compaction
- conversation state / tool-loop protocol

灰区采用“机制与结论分离”：API 文件保存机制，Model Profile 只保留它对 Prompt 的必要行为结论。

## Evals

回归测试现在分三层：

- `evals/core.json`：跨模型 Prompt 原则；
- `evals/models/<vendor>/*.json`：Prompt-relevant 模型行为；
- `evals/api/*.json`：冷加载的 API/协议规则。

本次拆分不增加测试数量：**总计仍为 45 个待执行 case**，只是把原来混在 Model eval 里的 API case 移到了 API eval。它们是测试输入与判定标准，不是模型真实通过记录。

## 示例

[worked-examples.md](examples/worked-examples.md) 默认只展示 Prompt 路径。API 示例单独位于 `examples/api/`，不会作为普通 Prompt 的默认材料。

## 静态校验

```bash
python3 scripts/validate.py
```

静态检查包括：Skill metadata、显式调用策略、Core/Model/API 分层、Model Profile 的 API boundary、API cold-load 声明、Markdown 相对链接、JSON eval 格式、case ID 唯一性和 API 示例契约。它不调用真实模型，因此不代表 Prompt 效果已经通过 replay eval。

## 安装当前开发分支

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo chrisjian/multi-model-prompt-writer \
  --ref prompt-quality-v1.1 \
  --path . \
  --name multi-model-prompt-writer
```

安装后显式使用 `$multi-model-prompt-writer`。

## 维护原则

当前资料核验日期：**2026-09-09**。要求“最新/官方”或可运行 API 配置时，应重新打开对应厂商官方资料，而不是把仓库快照当永久事实。

当前优先级是 Prompt 质量与真实 replay eval，而不是提前维护高变化率的 harness 配置百科。
