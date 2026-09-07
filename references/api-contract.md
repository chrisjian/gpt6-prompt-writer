# API 提示词与配置边界

仅在 API、Agent 或机器解析任务中读取。核验日期 2026-09-07；实际使用前按需复核官方页面。以下请求样例未经真实 API 调用。

## 已核验的 GPT‑6 限制

来源：[GPT‑6 Astra migration quickstart](https://developers.openai.com/api/docs/guides/latest-model#migration-quickstart)。

- API 模型 ID 使用 `gpt-6-astra`，不使用 `gpt6` 或猜测的 `gpt-6`。
- GPT‑6 Astra 的工具调用需要 **Responses API**。不能把带工具的 Chat Completions 请求只替换模型名就当成迁移完成；无工具的 Chat Completions 并非一概不支持。
- 删除 `temperature`、`top_p`、`top_logprobs`。Chat Completions 还应删除 `logprobs`；Responses 的 `include` 不使用 `message.output_text.logprobs`。
- 不设置 `none` 推理档位。旧配置为 `none` 或 `minimal` 时，官方建议从 `low` 开始比较；其他已有有效档位先保留。
- 不从其他模型或 Codex UI 推断 API 的全部档位和默认值。未核验的设置不输出为可运行配置。

## 最小 Responses 请求

下面是发往 `POST /v1/responses` 的 JSON 请求体示例，输入是合成材料。认证由调用应用配置，不把凭据写入提示词。

```json
{
  "model": "gpt-6-astra",
  "reasoning": {"effort": "low"},
  "instructions": "仅依据用户材料写一段中文通知。先说变化，再说影响与行动。保持简洁，不能添加材料没有的事实。",
  "input": "材料：周三例会从 10:00 调整到 11:00，地点不变。请提醒大家提前更新日历。"
}
```

这里的 `low` 是演示与比较起点，不是所有任务的最佳档位，也不宣称它是默认档位。难任务应在当前模型实际支持的选项中，通过任务评测平衡质量与延迟。[Reasoning effort](https://developers.openai.com/api/docs/guides/reasoning#reasoning-effort)

## 指令、输入与状态

稳定规则放 `instructions`，或改用 `input` 中的 developer 消息；用户本轮任务与资料用 user 输入承载。不要重复注入两份冲突的稳定指令。

API 角色决定权限，内容中写“这是 system prompt”不能提升权限。外部文档不应直接拼入高权限指令当作规则。

使用 `previous_response_id` 时，前一轮的 `instructions` 不会自动继承到当前请求；调用方须在需要的每轮重新传入稳定指令。不能仅靠“记住以上规则”替代状态管理。[Message roles](https://developers.openai.com/api/docs/guides/prompt-engineering#message-roles-and-instruction-following)

## 严格结构化输出

完整示例在 `../examples/extraction-request.json`。Responses 使用 `text.format`：`type: "json_schema"`、名称、`strict: true` 和 schema。不要把 Chat Completions 的 `response_format` 嵌套照搬进 Responses。

- 根 schema 是 object，不能以 `anyOf` 作为根。
- 每个 object 设置 `additionalProperties: false`。
- 对象所有 properties 均列入 `required`；允许缺失含义的字段用 nullable 类型等明确表达。
- 普通提示词要求“只输出 JSON”，或启用 JSON mode，都不能代替 schema 约束。
- 架构之外还有业务校验：事实依据、缺失值、状态与字段的一致性。
- 调用方先处理错误、拒绝与不完整响应，再解析成功结果；拒绝或截断不能冒充 schema 内的正常空结果。

来源：[Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)、[Supported schemas](https://developers.openai.com/api/docs/guides/structured-outputs#supported-schemas)。

## 工具与新能力

提示词只定义何时使用工具、范围和验收；工具必须由宿主提供并执行。不要把工具描述、虚构函数名或提示词里的 `async: true` 当成已完成集成。

需要异步工具、运行中追加指令或缓存相关配置时，先读取对应官方指南，再根据实际宿主生成集成建议；这些能力不应默认加入普通提示词：

- [Async tool calling](https://developers.openai.com/api/docs/guides/async-tool-calling)
- [Mid-turn steering](https://developers.openai.com/api/docs/guides/steering)
- [Change reasoning mid-conversation](https://developers.openai.com/api/docs/guides/reasoning#change-reasoning-mid-conversation)

本技能只核验了主指南对这些能力的介绍，未将详细事件协议纳入规则。用户未请求实现时，不改应用、开工具权限或运行 API。
