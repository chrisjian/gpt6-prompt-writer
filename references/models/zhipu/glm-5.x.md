# GLM 5.x Family Profile

Status: official-source verified 2026-09-09

本 Profile 面向 GLM‑5、5.1、5.2 等 5.x family。版本 API 能力变化明显，但这里只保留会直接改变 Prompt 写法的内容。

## Official sources

- https://docs.bigmodel.cn/cn/guide/models/text/glm-5
- https://docs.bigmodel.cn/cn/guide/models/text/glm-5.2
- https://docs.bigmodel.cn/cn/guide/platform/prompt
- https://docs.bigmodel.cn/cn/guide/start/migrate-to-glm-new

## Prompt-relevant behaviors / facts

- GLM 官方 Prompt Engineering 指南强调清晰具体指令、参考资料、复杂任务拆分、System Prompt、分隔符和必要 few-shot；这些原则与 Core 一致时无需重复堆叠。
- GLM 5.x 面向 Agentic Engineering / 长任务，但“更 Agentic”不意味着 Prompt 可以省略范围、完成标准或状态真实性。
- 官方旧 Prompt 教程中可能出现展示完整思维链类示例；不要把可见私密推理披露作为当前 Prompt 的质量要求。
- GLM 5.x 不同版本的 API/runtime 差异较大，因此版本-specific 参数不能反向改变通用 Prompt Core。

## Prompt adaptations

- 使用 Core 写明确任务、材料、约束、完成标准；只有实际失败需要时再补 GLM-specific 规则。
- 复杂 Agent 任务依赖实际接入提供的 thinking/tool 能力，不通过“展示每一步思考”替代。
- 参考资料、分隔符和 few-shot 只在任务需要时使用，不因为厂商指南列出就全部加入。
- 从旧 GLM prompt 迁移时重点删除私密 CoT 披露、无目的推理仪式和已不再对应失败模式的旧 workaround。

## API boundary

具体版本 context/output、thinking 默认、`reasoning_effort`、interleaved reasoning state、Function Calling、结构化输出和缓存见 [Zhipu GLM API reference](../../api/zhipu.md)。普通 Prompt 任务不加载该文件。

## Do not generalize

- 不把旧教程中的可见思维链示例当当前硬规则。
- 不把 GLM‑5.2 的 API 能力假定给整个 GLM 5.x family。
- 不因为 Agentic Engineering 定位而自动增加复杂编排、测试或 subagent 规则。
