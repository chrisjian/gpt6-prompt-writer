# DeepSeek V4 Family Profile

Status: official-source verified 2026-09-09

本 Profile 面向 DeepSeek V4 Pro / Flash family。Pro 与 Flash 共享主要 thinking/runtime 规则，variant 只记录能力/速度定位，不复制 Prompt Core。

## Official sources

- https://api-docs.deepseek.com/guides/thinking_mode/
- https://api-docs.deepseek.com/quick_start/pricing/
- https://api-docs.deepseek.com/api/create-response/
- https://api-docs.deepseek.com/api/create-chat-completion/
- https://api-docs.deepseek.com/updates/

## Verified model behaviors / facts

- 官方模型 ID 包括 `deepseek-v4-pro`、`deepseek-v4-flash`，另有 vision experimental variant。
- V4 thinking 默认开启，默认 effort 为 `high`。
- 原生 effort 主要为 `low / high / max`；兼容输入中 `medium`、`xhigh` 会映射到 `high`，Responses 兼容层还定义 `none/minimal` 等映射。
- thinking 模式下 `temperature`、`top_p`、`presence_penalty`、`frequency_penalty` 不生效；为兼容可能不会报错。
- thinking + tools 时，历史 `reasoning_content` 必须在后续请求正确回传，否则 API 可返回 400；没有 tools 时该字段无需回传并会被忽略。
- V4 Pro/Flash 官方服务为 1M context，并支持 JSON Output、Tool Calls、Responses API、Anthropic API。
- Flash 定位更快、更具成本效率；Pro 用于更强复杂任务。

## Prompt adaptations

- 不用 temperature/top_p 作为 thinking 模式的质量调节器；先决定是否 thinking，再选 effort。
- Agent/tool prompt 中把“保持 reasoning state”放入宿主/API 接入说明，不塞进给模型看的自然语言 Prompt。
- Pro/Flash 共用 Prompt Core；只有任务复杂度、延迟和成本要求影响 variant 选择。
- 旧 `deepseek-chat` / `deepseek-reasoner` 配置迁移时先核验当前 V4 model ID 与 thinking 开关，不只替换字符串。
- 结构化输出按当前接口能力核验；不要把 OpenAI Structured Outputs schema 语义直接假定为 DeepSeek JSON Output 语义。

## API / runtime notes

- Chat Completions：`thinking.type = enabled/disabled`，`reasoning_effort = low/high/max`。
- Responses compatibility：`reasoning.effort` 有兼容映射。
- Tool loop 必须正确保存/回传 reasoning state。
- 参数行为会随兼容接口不同而异，交付可运行请求时必须按目标接口核验。

## Variant notes

### Pro
复杂 reasoning / Agent 任务优先。

### Flash
简单 Agent 任务可接近 Pro，速度/成本更优；不要因此自动删减业务约束。

## Migration notes

- 旧模型迁移时重点检查 model ID、thinking 默认开启、effort 映射、sampling 参数失效与 tool-loop reasoning state。
- OpenAI/Anthropic compatibility 只表示协议兼容，不表示提示词行为完全相同。

## Do not generalize

- 不把 DeepSeek 的 `reasoning_content` 回传规则迁移给其他厂商。
- 不把 `medium → high` 映射当成通用 reasoning 语义。
- 不因为兼容 OpenAI/Anthropic API 就复制对应模型 Profile。
