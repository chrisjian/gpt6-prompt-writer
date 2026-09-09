# Gemini 3.x Family Profile

Status: official-source verified 2026-09-09

本 Profile 面向 Gemini 3 系列。具体型号和 preview/stable 状态变化较快；这里只保留会直接改变 Prompt 写法的行为结论。

## Official sources

- https://ai.google.dev/gemini-api/docs/gemini-3
- https://ai.google.dev/gemini-api/docs/models

## Prompt-relevant behaviors

- Google 明确建议 Gemini 3 prompt 直接、清晰、简洁。
- 从 Gemini 2.5 迁移时，应优先删除为了强迫推理而写的复杂 chain-of-thought prompt；不要把固定 step-by-step、反思轮次或可见思维链当成必要脚手架。
- 大量长上下文材料与最终具体任务应清楚分隔；具体问题靠近材料之后通常更不容易被前置背景淹没。
- Gemini 3 默认回答可能比用户预期更简洁；需要长文、展开论证或固定结构时应明确交付形状，而不是只写“深入一点”。

## Prompt adaptations

- 在 Core 之后优先做减法：删除旧式推理仪式，保留目标、硬约束、材料边界和完成标准。
- 长上下文任务使用明显的材料边界，并把最终问题/动作要求放在材料之后。
- 需要更详细输出时明确篇幅、层次或必备信息。
- 涉及外部工具时只要求使用宿主真实提供的能力，不把提示词当工具开关。

## API boundary

`thinking_level`、temperature、thought signatures、兼容层 reasoning 映射、具体 context/output 和工具协议见 [Google Gemini API reference](../../api/google.md)。普通 Prompt 写作不加载该文件。

## Migration notes

Gemini 2.5 → 3.x 的 Prompt 迁移重点是重新证明旧 reasoning scaffolding 的必要性；没有真实失败证据时优先删除，而不是机械保留。

## Do not generalize

- 不把 Gemini 的 Prompt 简化建议理解成所有复杂任务都必须极短。
- 不把长上下文排布规则机械套给没有长材料的任务。
- 不把 Gemini API 的 thinking/sampling/state 机制迁移给其他厂商。
- 不要求输出私密思维链。
