# GLM 5.x Family Profile

Status: official-source verified 2026-09-09

本 Profile 面向 GLM‑5、5.1、5.2 等 5.x family。版本能力变化明显，因此 family 共性之外必须按具体版本收窄参数。

## Official sources

- https://docs.bigmodel.cn/cn/guide/models/text/glm-5
- https://docs.bigmodel.cn/cn/guide/models/text/glm-5.2
- https://docs.bigmodel.cn/cn/guide/capabilities/thinking
- https://docs.bigmodel.cn/cn/guide/capabilities/thinking-mode
- https://docs.bigmodel.cn/cn/guide/start/migrate-to-glm-new
- https://docs.bigmodel.cn/cn/guide/platform/prompt

## Verified model behaviors / facts

- GLM 5.x 面向 Agentic Engineering / 长任务；GLM‑5.2 官方页面为 1M context、128K max output，GLM‑5 页面为 200K context。
- GLM‑5.2 / 5.1 / 5 等默认开启 thinking；官方 thinking-mode 文档说明 GLM 4.6 的默认行为不同，因此不能把 5.x 规则回套早期版本。
- 从 GLM 4.5 起支持 interleaved thinking；工具调用时必须显式保留 reasoning content 并与工具结果一并回传。
- `reasoning_effort` 当前仅 GLM‑5.2 及以上支持；官方列出 `max/xhigh/high/medium/low/minimal/none`，并有映射规则：none/minimal 放弃思考，low/medium 映射 high，xhigh 映射 max；默认推荐 max。
- GLM 官方 Prompt Engineering 指南强调清晰具体指令、参考资料、复杂任务拆分、System Prompt、分隔符和 few-shot；其中“展示完整思维链”类旧式示例不能覆盖本 Skill 的推理隐私边界。
- GLM 5.x 支持 Function Calling、结构化输出、上下文缓存等能力；具体版本仍需核验。

## Prompt adaptations

- 先写明确任务、材料、约束、完成标准；复杂 Agent 任务可使用模型 thinking/runtime，而不是在 Prompt 中强制展示内部推理。
- 使用 GLM‑5.2 时才能默认考虑 `reasoning_effort`；GLM‑5/5.1 不应伪装支持该参数。
- 工具/Agent 场景把 interleaved reasoning state 的保留放入 runtime adapter，不写成用户可见 Prompt 内容。
- 从 GLM 官方旧 Prompt 教程吸收“清晰、具体、参考资料、必要 few-shot”，但不采用“展示每一步私密思维链”作为质量要求。
- 大上下文任务使用具体版本真实 context；不要把 GLM‑5.2 的 1M 假定给 GLM‑5。

## API / runtime notes

- `thinking.type = enabled/disabled`。
- `reasoning_effort`：仅 GLM‑5.2+。
- tool/function calling 的 reasoning state 需要正确拼接。
- `temperature/top_p` 的迁移建议按具体版本官方 migration 页面核验。

## Variant notes

### GLM-5
200K context；支持 thinking/function call/cache/structured output，但不要套用 5.2-only reasoning_effort。

### GLM-5.1
沿用 5.x family 行为时仍需按官方当前模型页核验版本差异。

### GLM-5.2
1M context、128K output；支持 `reasoning_effort`，适合长程 coding/agent。

## Migration notes

- 4.x → 5.x 时重点检查 thinking 默认行为。
- 5/5.1 → 5.2 时检查 1M context、reasoning_effort、tool streaming 与采样参数建议。

## Do not generalize

- 不把 GLM‑5.2 的 1M context、reasoning_effort 默认值写成整个 GLM 5.x 永久事实。
- 不要求模型披露私密思维链，即使厂商旧 Prompt 教程包含这类示例。
- 不把 GLM interleaved reasoning state 机制迁移给其他 API。
