# Prompt Engineering Core

本文件只记录跨模型通用的工程原则。模型专属倾向、API 字段和迁移要求必须放在 `references/models/` 下的对应 Profile。

## 1. 最小任务契约

一个稳定提示词优先回答：

- 要完成什么。
- 面向谁。
- 输入/材料是什么。
- 任务用途是什么（仅当用途会改变重点、取舍、风险或输出结构）。
- 哪些约束真正影响结果。
- 交付物是什么形状。
- 什么状态算完成。
- 缺失信息如何处理。
- 可用工具与授权边界是什么（若涉及）。

不要为了形式完整而强制每个任务拥有所有字段。

## 2. 结果与验收优先

把“专业、深入、高质量、认真检查”转成可观察结果，例如：必需内容、证据要求、篇幅、事实边界、验证结果或失败分支。

完成标准描述结果状态，不描述固定思考轮次、自评分或重复复核次数。

## 3. 根因级指令优先

如果多个失败表现能由同一行为原则控制，优先写一条明确、正向的根因规则。

例如，与其分别禁止“重复总结、列无关方案、长篇背景、无用过渡”，更适合写：只保留会改变读者理解、判断或下一步行动的信息，先给结果，再给必要支持。

## 4. Purpose 条件化

说明“为什么做”通常能改善复杂任务的取舍，但 Purpose 不是必填背景栏。只有用途会改变信息筛选、优先级、风险判断或交付形状时才写入。

## 5. 意图边界

先判断用户要的是分析、建议还是执行：

- 描述问题、提问、思考或明确只诊断：交付 assessment，不自行改变外部状态。
- 明确请求修复、修改、发送、执行等行动：在已授权边界内执行，不降级成能力说明或重复确认。

自主性不能替代意图判断，意图判断也不能成为明确行动请求的拖延理由。

## 6. 状态不越级

“已读取、已搜索、已修改、已运行、已验证、已通过、已完成”等状态必须由实际输入、工具结果或可检查产物支持。

默认只报告必要状态，不展开完整日志或证据。用户要求审计、复现或核查时再展开。

## 7. Prompt Audit

优化旧提示词时检查：

- 语义重复。
- 症状级禁令堆叠。
- 模糊强化词。
- 相互冲突的硬约束。
- 无目的角色包装或固定流程。
- 为旧模型设计的 workaround。
- 宿主并不存在的工具、权限或运行时能力。

“过去有效”不是保留规则的充分理由。保留模型 workaround 需要当前 Profile、实际 eval 或明确失败模式支持。

## 8. Behavior-preserving compression

压缩的目标是减少 instruction surface area 和冲突面，而不是单纯缩短字符。

优先顺序：删除重复 → 合并根因 → 删除无效强化 → 收窄触发条件 → 用结果/验收替代过程口号 → 缩短冗长例子 → 最后精简措辞。

压缩不变量：目标、事实边界、权限、关键输入、输出格式、缺失信息处理、失败分支和真正影响结果的约束。

## 9. 可读性优先于电报体

输出简洁优先通过删除不影响理解、判断或行动的信息实现，而不是依赖句子残片、过度缩写、箭头链、术语堆积或人为标签。

如果“更短”和“更清楚”冲突，优先清楚，除非用户给了更高优先级的长度硬约束。

## 10. 正例按需

文字规则已经明确但某种微妙行为仍容易误解时，优先增加一个短而代表性的正确示例，而不是继续增加近义禁令。

不默认 few-shot。示例应解决真实歧义，不重复已经清楚的规则。

## 11. 事实、行为、模型与宿主分层

- 来源支撑事实。
- Prompt 定义行为。
- Model Profile 描述特定模型当前官方指南、已知倾向与 API 事实。
- Runtime / host 决定工具、权限、状态、异步、缓存、子代理等是否真实存在。

提示词文字不能把不存在的能力变成存在。

## 12. 模型特例不可泛化

每个 Model Profile 都必须包含 `Do not generalize`。任何厂商专属默认 effort、格式倾向、验证倾向、搜索行为或 API 字段，都不能自动传播到其他模型或通用 Core。

## 来源与证据边界

这些原则是本项目的工程归纳，不宣称是某一家厂商统一规定。当前依据包括：

- OpenAI GPT‑6 Astra model guidance: https://developers.openai.com/api/docs/guides/latest-model
- Anthropic Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic Claude Fable 5: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- Anthropic Claude Fable 5.1: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
- xAI Grok 4.6 model/API docs: https://docs.x.ai/developers/grok-4-6

厂商页面中的模型特有行为只进入对应 Profile；只有可合理泛化、且不依赖专属参数或已测倾向的工程原则才进入 Core。
