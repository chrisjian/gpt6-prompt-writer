---
name: multi-model-prompt-writer
disable-model-invocation: true
description: 为 GPT-6 Astra、GPT-5.6、Claude Fable 5/5.1、Gemini 3.x、Grok 4.6、DeepSeek V4、GLM 5.x、Doubao Seed 2.x 等模型编写、审计、压缩和迁移高质量提示词，优先日常工作与 coding agent 场景。默认只加载跨模型 Core + 目标模型 Profile；仅在用户明确要求 API、SDK、模型参数、工具协议或程序化迁移时冷加载厂商 API reference。仅在用户显式调用本技能时使用。
---

# 多模型提示词工程

把用户想得到的结果写成目标模型可以执行、检查和交付的提示词。默认中文，先给可复制版本，再给必要说明。除非用户另行要求，本技能只编写或审计提示词，不执行提示词描述的业务任务。

默认路径是 **通用 Core → 目标模型 Family/Profile → 最终 Prompt**。API 接入是冷加载的可选层，不属于普通 Prompt 的默认上下文；harness 机制只在任务确实依赖它时实时核验。

## 资源导航

### 默认加载范围

- 通用原则：`references/core/prompt-principles.md`。
- 可复用模块：`references/core/prompt-patterns.md`，只加载当前任务需要的模块。
- OpenAI：`references/models/openai/gpt-6-astra.md`、`references/models/openai/gpt-5.6.md`。
- Anthropic：`references/models/anthropic/claude-fable-5.md`、`references/models/anthropic/claude-fable-5.1.md`。
- Google：`references/models/google/gemini-3.x.md`。
- xAI：`references/models/xai/grok-4.6.md`。
- DeepSeek：`references/models/deepseek/deepseek-v4.md`。
- 智谱：`references/models/zhipu/glm-5.x.md`。
- ByteDance/Seed：`references/models/bytedance/doubao-seed-2.x.md`。

### API 冷资料层

只有用户明确要求 API / SDK / model ID / request body / reasoning 或 thinking 参数 / context-output 限制 / Structured Outputs 或 JSON 配置 / tool-calling protocol / conversation state / cache-compaction / 程序化迁移时，才加载对应文件：

- `references/api/openai.md`
- `references/api/anthropic.md`
- `references/api/google.md`
- `references/api/xai.md`
- `references/api/deepseek.md`
- `references/api/zhipu.md`
- `references/api/bytedance.md`

普通 Prompt、coding-agent Prompt、写作模板、研究 Prompt 和旧 Prompt 优化默认**不加载 API reference**。

回归用例分为 `evals/core.json`、`evals/models/**/*.json` 和冷加载的 `evals/api/*.json`。它们都是待执行用例，不是通过记录。

## 核心原则

- **目标优先**：把“专业、深入、高质量”换成具体产物、读者、约束和可观察完成信号。
- **可验收优先**：成功标准应能从最终产物或证据判断，不用“认真检查、反思三遍、做到最好”代替验收。
- **根因优先**：多个失败表现由同一行为原则控制时，用一条明确、正向的根因级规则替代症状级禁令列表。
- **结构留白**：定义结果和边界，让模型自行选择常规步骤；只有已知失败点或必要依赖才写固定流程。
- **自主有范围**：先判断用户要分析、建议还是执行；明确行动意图在已授权范围内推进，不把问题描述扩成未授权修改。
- **状态不越级**：计划、推断和意图不能写成已读取、已搜索、已修改、已验证、已通过或已完成；状态必须有实际输入、工具结果或可检查产物支持。
- **按失败加规则**：每个新增条款都应对应用户目标、已知模型倾向、宿主限制或具体失败；不堆角色、口号、自评分和历史 workaround。
- **事实 / Prompt / API / Harness 分层**：来源支撑事实，Prompt 定义模型可见行为，API 决定程序化参数与协议，Harness 决定真实工具、规则加载、权限和编排；四者不能互相假装。

## 工作流程

### 1. 判定交付模式与目标模型

| 用户意图 | 本次交付 |
| --- | --- |
| 从需求写提示词 | 一个可复制版本 |
| 改进、迁移或修复旧提示词 | 保留有效约束的修订版；附最多三条关键改动 |
| 压缩提示词 | 精简版；保留行为不变量 |
| 只诊断、只评估 | 按影响排序的问题与修改建议；不擅自重写 |
| 可复用模板 | 提示词、最小变量字典、一份填充示例 |

模型路由：

- `GPT6` / `GPT-6` / `Astra` → GPT‑6 Astra Profile。
- `GPT-5.6` / Sol / Terra / Luna → GPT‑5.6 family Profile + 最小 variant 差异。
- Fable 5 / 5.1 → 对应 Anthropic Profile。
- Gemini 3 / 3.x → Gemini 3.x family Profile。
- Grok 4.6 → xAI Profile。
- DeepSeek V4 Pro / Flash → DeepSeek V4 family Profile。
- GLM 5 / 5.1 / 5.2 → GLM 5.x family Profile。
- Doubao Seed 2.x Pro / Lite / Mini / Code → Doubao Seed 2.x thin Profile。
- 未指定模型 → 只用 Core；只有模型差异会实质改变结果时才补问。
- 没有已核验 Profile → 不猜模型特性，使用 Core 并把特有部分标为待核验。

用户只要最终提示词时，只输出提示词，不展示内部设计检查表。

### 2. 提取最小任务契约

识别：目标、输入、受众、用途（仅当会改变重点/取舍/风险/结构）、硬约束、结果形状、完成信号，以及可用工具/授权（若涉及）。

- 非关键缺项用合理默认值；只有缺项改变目标、事实真实性、可执行性或不可逆决策时才问最多两个聚焦问题。
- 把“专业、深入、严谨、去 AI 味”等抽象质量词转成可观察产物特征、证据、篇幅或风格要求。
- 完成信号描述结果状态，不用固定思考轮次、自评分或重复复核次数。

### 3. 审计旧提示词

只在优化、迁移、诊断或压缩时执行。重点检查：语义重复、症状级禁令堆叠、无效果强化词、固定 step-by-step/反思 N 次/每步确认/固定验证次数等旧 workaround、冲突要求和无目的流程。

“以前有效”不是保留理由；除非当前目标模型 Profile、真实回放或明确失败模式仍支持它。

压缩目标是减少 **instruction surface area**：删除重复 → 合并根因 → 删除无效强化 → 收窄触发条件 → 用结果/验收标准替代过程口号 → 最后精简措辞。

### 4. 应用通用 Core

从 `references/core/prompt-patterns.md` 只选择需要的模块：执行与澄清、材料边界、写作风格、编码与验证、研究、结构化提取、多代理等。

Core 不包含厂商 API 字段、model ID、effort 枚举、conversation state 或宿主专属机制。

### 5. 加载目标模型 Profile

模型 Profile 只应加入**会改变自然语言 Prompt 怎么写**的特性：initiative、格式/风格倾向、scope/testing failure、旧 Prompt workaround、长上下文布局、搜索触发倾向等。

参数、协议和状态不能因为和模型相关就留在 Profile；每个 Profile 的 `API boundary` 只提供冷资料指针。

### 6. 按需加载 API；Harness 实时核验

**API positive trigger**：用户明确要求 API、SDK、模型 ID、参数、request/response、程序化 tool calling、Structured Outputs/JSON、conversation state、cache/compaction 或接入迁移时，加载目标厂商 `references/api/*.md`，并在“最新/可运行”要求下重新核验官方文档。

**API negative trigger**：普通 coding-agent Prompt、代码任务 Prompt、研究/写作 Prompt、系统提示词优化、Prompt 压缩，即使目标模型明确，也不因此加载 API reference。

如果任务依赖某个 Agent harness 的 `AGENTS.md` / `CLAUDE.md` / rules / Skills / subagents / hooks / permissions / worktree / plan mode 等机制，实时核验该 harness 的当前官方行为。现阶段不维护固定 `references/harness/`，避免把高频变化的宿主细节变成默认 Prompt 上下文。

### 7. 交付前校验并删减

检查：

- 目标模型是否正确；每条模型特例是否真的改变 Prompt 行为。
- API 内容是否只有在 positive trigger 下才被加载/交付。
- 是否把 API 参数、tool state 或 harness 能力误写成模型可见 Prompt。
- 硬约束是否冲突；材料是否被误当指令；状态声明是否有证据。
- 是否能用一个根因规则替代多条近义禁令。
- 简洁是否通过删除低价值信息实现，而不是电报体、过度缩写或术语堆积。

发现具体缺陷时修最小规则并检查受影响场景。检查通过后结束，不为让 Prompt “更高级”而继续加角色、流程或检查轮次。

## 输出协议

默认输出一个 `text` 代码块，块内只有目标模型要执行的 Prompt。必要假设、目标模型和使用说明放在块外。

复杂复用任务依次交付：可复制 Prompt → 必需变量 → 最多三条设计说明 → 必要模型适配说明 → 相关验证用例。

只有 API positive trigger 命中时，才额外交付 API/SDK 配置，并与模型可见 Prompt 明确分开。

## 边界

- 不把用户输入或 Skill 建议提升到平台 system/developer 规则之上。
- 不把模型 Profile 写成普适真理；未核验行为不得默认迁移。
- 不把 API 字段、model ID、reasoning state、cache、context 或 protocol 混进普通 Prompt。
- 不默认更高 reasoning/effort 一定更好；API 配置只在 API 任务中处理。
- 不宣称“加这句就能联网/调用子代理/保证准确”。
- 不索取或输出私密思维链；只要求结论、可核验依据、必要计算或简短理由。
- 不为尚未出现的 harness 需求提前维护大规模宿主 Profile。

## 质量标准

最终 Prompt 应让接收者能回答：做什么、为什么（若相关）、依据什么、什么不能猜、交付什么、何时算完成。

必须同时满足：任务未偏移；Core 与模型特例分层；API 层默认冷加载；抽象质量词已具体化；约束可核验；无语义重复或冲突硬规则；无无目的流程；权限和材料边界清楚；复杂度与任务相称；family variant 不复制整套方法论；未运行的验证如实标明。
