# 多模型提示词写作示例

以下是合成设计示例，不是独立模型运行结果。默认示例聚焦 Prompt；API 示例单独冷存放。

## 1. 未指定模型：只使用 Core

用户：优化这个 prompt：“请非常专业、深入、认真地比较 A 和 B。”结果要给技术负责人决定未来两年的主力方案。

```text
比较 A 和 B，供技术负责人决定未来两年的主力方案。

重点评估会影响两年期决策的因素：维护成本、长期兼容性、生态成熟度、团队迁移成本、关键能力差异和锁定风险。对每个关键判断给出具体理由或可核验依据；事实不足时明确未知，不用“更先进、更专业”等空泛词替代判断。

先给推荐结论和适用前提，再比较关键维度、主要风险和推荐下一步。只保留会改变决策的信息。
```

这里没有目标模型，因此不加入任何模型特有规则。

## 2. GPT‑6 Astra：控制过度验证

用户：给 GPT‑6 Astra 写 coding-agent prompt，修一个低影响 UI 文案 bug，不要每次都全量测试。

设计时使用 Core + `references/models/openai/gpt-6-astra.md`：保留项目必需检查和受影响行为验证，但只有新改动、失败或具体未决风险才扩大测试。不会因为目标是 GPT‑6 就加载 `references/api/openai.md`。

## 3. Claude Fable 5.1：当前事实 + low effort

用户：给 Fable 5.1 写一个低 effort 研究 prompt，回答今天的产品更新。

设计时使用 Core + `references/models/anthropic/claude-fable-5.1.md`：因为 Anthropic 当前记录 low effort 下搜索触发可能更弱，应明确要求使用宿主实际提供的搜索/检索工具核实当前事实；这条不能传播到其他模型。

## 4. Grok 4.6：当前事实

用户：给 Grok 4.6 写今天 AI 新闻的研究 prompt。

设计时使用 Core + `references/models/xai/grok-4.6.md`：要求在宿主实际启用时使用 Web Search / X Search 等当前信息来源，并明确没有搜索能力就不能把模型记忆当作今天的数据。不要凭经验添加“少 Markdown、多 delegation、少测试”等未经证据支持的倾向。

## 5. API 请求：单独冷加载

只有用户明确要求“给我 GPT‑6 Structured Outputs 的请求体/SDK 配置”时，才额外加载 `references/api/openai.md`。合成 API 示例见 [openai-extraction-request.json](api/openai-extraction-request.json)。它不是普通 Prompt 任务的默认模板。
