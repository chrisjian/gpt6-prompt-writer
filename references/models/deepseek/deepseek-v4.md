# DeepSeek V4 Family Profile

Status: official-source verified 2026-09-09

本 Profile 面向 DeepSeek V4 Pro / Flash family。API 文档对 thinking/runtime 的说明很充分，但自然语言 Prompt 行为证据相对有限，因此只保留能直接改变 Prompt 设计的结论。

## Official sources

- https://api-docs.deepseek.com/guides/thinking_mode/
- https://api-docs.deepseek.com/updates/

## Prompt-relevant behaviors / facts

- V4 提供原生 thinking 能力，因此没有必要通过固定 `think step by step`、反思 N 次、展示内部推理等旧式仪式重复强迫 reasoning。
- Pro 定位更强复杂任务；Flash 优先速度/成本。当前没有足够依据要求两者维护两套不同的自然语言 Prompt 方法论。
- API compatibility 不代表行为完全等同于 OpenAI 或 Anthropic 模型；不要复制对应 Model Profile。

## Prompt adaptations

- 先使用通用 Core：清晰任务、材料、约束、完成标准和失败处理。
- 需要复杂推理时使用实际接入提供的原生 thinking 配置，而不是增加可见思维链要求。
- Pro/Flash 共用 Prompt Core；variant 只在任务复杂度、延迟和成本选择上发挥作用，除非真实 eval 证明 Prompt 行为不同。
- Tool/Agent 任务只描述模型需要执行的行为，不要求模型自行维护 API conversation state。

## Variant notes

### Pro
复杂 reasoning / Agent 任务优先。

### Flash
速度/成本优先；不要因此自动删减事实边界、约束或验收标准。

## API boundary

Model ID、thinking 默认值、effort 映射、sampling 参数行为、`reasoning_content`、context、JSON/tool protocol 和兼容接口见 [DeepSeek API reference](../../api/deepseek.md)。普通 Prompt 工作不加载该文件。

## Do not generalize

- 不把 DeepSeek API 的 reasoning-state 机制写进其他模型 Profile。
- 不因为协议兼容就复制 OpenAI/Anthropic prompting workaround。
- 不声称 Pro/Flash 需要完全不同的 Prompt，除非后续官方资料或 eval 支持。
