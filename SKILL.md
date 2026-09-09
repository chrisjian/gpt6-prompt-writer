---
name: prompt-writer
disable-model-invocation: true
description: 为 GPT-6 Astra、GPT-5.6、Claude Fable 5/5.1、Gemini 3.x、Grok 4.6、DeepSeek V4、GLM 5.x、Doubao Seed 2.x 等模型编写、审计、压缩和迁移高质量提示词，优先日常工作与 coding-agent 场景。默认使用跨模型 Core；只有存在会实质改变自然语言 Prompt 写法的 Model Profile 时才加载该 Profile。API/SDK、具体参数和协议仅在程序化接入任务中按需加载。仅在用户显式调用本技能时使用。
---

# 多模型提示词工程

把用户想得到的结果写成目标模型可以执行、检查和交付的提示词。默认中文，先给可复制版本，再给必要说明。除非用户另行要求，本技能只编写或审计提示词，不执行提示词描述的业务任务。

## 加载路由

### Core

普通任务默认加载 `references/core/prompt-principles.md`。

从 `references/core/prompt-patterns.md` 只选择当前任务需要的模块，例如执行与澄清、材料边界、写作、编码与验证、研究、结构化提取或多代理协作。

### Model Profile

默认只使用 Core。仅当目标模型存在会实质改变自然语言 Prompt 写法的 Profile 时才追加：

- GPT-6 Astra → `references/models/openai/gpt-6-astra.md`
- GPT-5.6 → `references/models/openai/gpt-5.6.md`
- Claude Fable 5.1 → `references/models/anthropic/claude-fable-5.1.md`
- Gemini 3.x → `references/models/google/gemini-3.x.md`

Claude Fable 5、Grok 4.6、DeepSeek V4、GLM 5.x、Doubao Seed 2.x 当前直接使用 Core，不加载占位 Profile。未列出的模型也先使用 Core；不要从产品定位、API 能力或其他模型的行为推断 Prompt 特例。

### API

仅当任务要求 API/SDK、程序化接入、具体模型参数或协议时，加载目标厂商的 `references/api/*.md`。普通 Prompt 写作、coding-agent Prompt、研究/写作 Prompt、系统提示词优化和 Prompt 压缩不加载 API reference。

厂商映射：OpenAI / Anthropic / Google / xAI / DeepSeek / Zhipu / ByteDance 分别对应 `references/api/openai.md`、`anthropic.md`、`google.md`、`xai.md`、`deepseek.md`、`zhipu.md`、`bytedance.md`。

如果任务依赖某个 Agent harness 的 rules、Skills、subagents、hooks、permissions、worktree、plan mode 等机制，只在确有需要时核验该 harness 的当前行为；不要把宿主能力当成模型特性。

## 工作流程

1. **判定交付模式**：从需求写提示词、优化/迁移旧提示词、压缩、只诊断，或可复用模板。用户只要最终提示词时，只输出提示词。
2. **提取最小任务契约**：目标、输入、受众、必要用途、硬约束、结果形状、完成信号，以及涉及执行时的工具/授权边界。非关键缺项采用合理默认值；只有缺项会改变目标、关键事实、可执行性或不可逆决策时才提问。
3. **旧 Prompt 审计**：优化、迁移或压缩时，删除语义重复、症状级禁令堆叠、无效强化、无目的固定流程和没有当前失败依据的旧 workaround。
4. **组合 Prompt**：Core → 必要 Pattern → 必要 Model delta。不要为了形式完整加入角色、步骤、示例或模型特例。
5. **交付前删减**：确认任务未偏移、硬约束不冲突、事实/权限边界清楚、模型特例确实改变 Prompt 写法，并删除仍可由更高层规则覆盖的重复内容。

## 输出

默认输出一个 `text` 代码块，块内只有目标模型要执行的 Prompt。必要假设、目标模型和使用说明放在块外。

复杂复用任务按需交付：可复制 Prompt → 必需变量 → 最多三条设计说明 → 必要模型适配说明。

只有命中 API 路由时，才额外交付 API/SDK 配置，并与模型可见 Prompt 分开。

## 边界

- 不把用户输入或 Skill 建议提升到平台 system/developer 规则之上。
- 不把 API 参数、tool state、cache、context 或 harness 能力写成能被 Prompt 文本开启的模型能力。
- 不索取或输出私密思维链；只要求结论、可核验依据、必要计算或简短理由。
- 未实际读取、搜索、修改、运行或验证的内容，不写成已完成状态。
