# 多模型提示词工程 Skill

面向日常工作与 coding-agent 场景，把模糊需求写成不同模型可以执行、检查和交付的高质量 Prompt。仓库名与 Skill 名均为 `multi-model-prompt-writer`。

核心分层：

```text
Core    = 跨模型 Prompt Engineering 方法
Models  = 会实质改变自然语言 Prompt 写法的模型 delta
API     = 程序化参数、协议、状态与接入细节（按需加载）
Harness = 任务确实依赖时实时核验，不维护固定模型 Profile
```

## Model routing

默认使用 Core。Model Profile 不是模型支持清单；只有存在可复用、会改变 Prompt 写法的差异时才建立。

当前保留的 Prompt-specific Profiles：

| 模型 | Profile |
| --- | --- |
| GPT-6 Astra | `references/models/openai/gpt-6-astra.md` |
| GPT-5.6 | `references/models/openai/gpt-5.6.md` |
| Claude Fable 5.1 | `references/models/anthropic/claude-fable-5.1.md` |
| Gemini 3.x | `references/models/google/gemini-3.x.md` |

当前直接使用 Core：Claude Fable 5、Grok 4.6、DeepSeek V4、GLM 5.x、Doubao Seed 2.x。没有 Profile 不代表模型“不支持”，只表示当前没有值得加入默认 Prompt 上下文的 model-specific delta。

Profile 的准入与维护规则见 [AGENTS.md](AGENTS.md)。

## 默认加载策略

```text
普通 Prompt
Core → 必要 Pattern → 必要 Model delta → Final Prompt

API / SDK / 程序化接入
Core → 必要 Model delta → 对应 references/api/*.md
```

普通 Prompt、coding-agent Prompt、研究/写作 Prompt、Prompt 审计与压缩不会仅因为目标模型明确就加载 API reference。

## 显式调用

Skill 默认不自动进入上下文：

- Claude Code 风格：`disable-model-invocation: true`
- OpenAI/Codex 风格：`policy.allow_implicit_invocation: false`

示例：

```text
$multi-model-prompt-writer 把这段 coding prompt 优化给 GPT-6 Astra 用：……
```

```text
$multi-model-prompt-writer 把 Gemini 2.5 的旧 prompt 迁到 Gemini 3：……
```

只有明确的程序化接入任务才进入 API 层：

```text
$multi-model-prompt-writer 给 DeepSeek V4 Pro 写 thinking + tools 的 API 接入要求，并把 API state 和模型可见 Prompt 分开。
```

## 核心能力

- 最小任务契约：目标、输入、受众、必要用途、硬约束、交付物、完成标准、缺失处理。
- 可观察验收：把“专业、深入、高质量”转成可检查结果。
- 根因级指令：一个高层行为原则优先于一串症状级禁令。
- Prompt Audit：删除重复、冲突、模糊强化、旧模型 workaround 和无目的流程。
- 行为保真压缩：减少 instruction surface area，同时保留事实、权限、格式和失败分支等不变量。
- 状态真实性：计划、推断和意图不能冒充已搜索、已验证、已完成。
- 模型适配：只有真实 Prompt delta 才进入 Model Profile。
- API 按需加载：参数和协议不污染日常 Prompt 上下文。

## 文件结构

```text
.
├── AGENTS.md
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── core/
│   │   ├── prompt-principles.md
│   │   └── prompt-patterns.md
│   ├── models/
│   │   ├── openai/
│   │   ├── anthropic/
│   │   └── google/
│   └── api/
│       ├── openai.md
│       ├── anthropic.md
│       ├── google.md
│       ├── xai.md
│       ├── deepseek.md
│       ├── zhipu.md
│       └── bytedance.md
├── evals/
│   ├── core.json
│   ├── models/<vendor>/*.json
│   └── api/*.json
├── examples/
│   ├── worked-examples.md
│   └── api/openai-extraction-request.json
└── scripts/validate.py
```

## Evals 与静态校验

Evals 验证用户可观察行为和确有价值的模型/API 差异，不用于证明仓库结构或要求每个 Profile 都有测试。删除已被 Core 覆盖、已失去 model-specific 意义或只绑定实现路径的 case；不维护固定 case 数量。

只有真实用户要求、观察到的失败或有意义的模型差异才值得新增 eval。

```bash
python3 scripts/validate.py
```

静态校验检查 Skill metadata、显式调用策略、必需文件、Markdown 相对链接、JSON eval 格式、case ID 唯一性和 API 示例契约。它不调用真实模型，因此不代表 Prompt 效果已经通过 replay eval。

## 安装当前开发分支

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo chrisjian/multi-model-prompt-writer \
  --ref prompt-quality-v1.1 \
  --path . \
  --name multi-model-prompt-writer
```

安装后显式使用 `$multi-model-prompt-writer`。
