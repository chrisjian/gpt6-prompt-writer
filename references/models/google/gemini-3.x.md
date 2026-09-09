# Gemini 3.x Family Profile

Status: official-source verified 2026-09-09

本 Profile 面向 Gemini 3 系列。具体型号与 preview/stable 状态变化较快；用户要求可运行配置时重新核验模型页。

## Official sources

- https://ai.google.dev/gemini-api/docs/gemini-3
- https://ai.google.dev/gemini-api/docs/models

## Verified model behaviors / facts

- Gemini 3 系列使用动态 thinking；`thinking_level` 控制最大思考深度，当前官方文档默认 `high`。
- Google 明确建议 Gemini 3 prompt 直接、清晰、简洁；从 Gemini 2.5 迁移时，应尝试删除为了强迫推理而写的复杂 chain-of-thought prompt，并用模型 thinking 控制替代。
- 官方强烈建议 Gemini 3 保持 temperature 默认 `1.0`；降低 temperature 可能导致循环或复杂推理性能下降。
- Stateful Interactions API 可自动管理 thought signatures；手动管理 stateless history 时需要正确保留 thought blocks/signatures。
- Gemini 3 支持 built-in tools 与 function calling 组合；Computer Use 不再需要单独的 2.5 专用模型。
- OpenAI compatibility layer 会把标准 reasoning effort 映射为 Gemini thinking level。

## Prompt adaptations

- 在通用 Core 之后优先做“减法”：删除旧式 `think step by step`、固定反思轮次等为了旧模型强迫 reasoning 的过程提示。
- 复杂任务主要通过清晰目标、硬约束、材料边界、完成标准与 `thinking_level` 控制，不额外堆推理仪式。
- 长上下文任务把大量材料与最终具体问题清楚分隔；具体任务尽量靠近材料之后。
- 需要更长、更展开的回答时明确篇幅/结构，不用空泛“深入一点”替代输出标准。
- 需要工具时只描述真实启用的 grounding/function/computer-use 能力，不把提示文字当工具开关。

## API / runtime notes

- `thinking_level` 是 Gemini-native 控制；兼容层可能映射 OpenAI reasoning effort。
- temperature 默认 `1.0` 是当前官方推荐起点。
- thought signatures 属于 conversation/runtime state，不应被写成自然语言 Prompt 规则。
- 具体 context、输出上限和可用型号以最新 models 页面为准。

## Migration notes

- Gemini 2.5 → 3.x：优先移除人为 chain-of-thought forcing，使用简化 Prompt + thinking control。
- 迁移旧代码时审计显式低 temperature。
- 多模态任务还需核验 media resolution 与具体模型能力。

## Do not generalize

- 不把 temperature=1.0 的建议迁移到其他厂商。
- 不把 Gemini thought signatures 当成通用 conversation-state 机制。
- 不声称所有 Gemini 3 型号具有完全相同工具、context 或发布状态。
- 不要求输出私密思维链；thinking 参数与可见解释不是同一件事。
