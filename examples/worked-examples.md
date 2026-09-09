# 多模型提示词写作示例

以下是合成设计示例，不是独立模型运行结果。默认示例聚焦 Prompt；API 示例单独存放。

## 1. 未指定模型：只使用 Core

用户：优化这个 prompt：“请非常专业、深入、认真地比较 A 和 B。”结果要给技术负责人决定未来两年的主力方案。

```text
比较 A 和 B，供技术负责人决定未来两年的主力方案。

重点评估会影响两年期决策的因素：维护成本、长期兼容性、生态成熟度、团队迁移成本、关键能力差异和锁定风险。对每个关键判断给出具体理由或可核验依据；事实不足时明确未知，不用“更先进、更专业”等空泛词替代判断。

先给推荐结论和适用前提，再比较关键维度、主要风险和推荐下一步。只保留会改变决策的信息。
```

这里没有目标模型，因此不加入模型特有规则。

## 2. GPT-6 Astra：多代理委派

用户：给 GPT-6 Astra 写一个 coding-agent prompt，宿主已经提供 subagents，希望独立任务能并行处理。

设计时使用 Core + `references/models/openai/gpt-6-astra.md`。Core 定义任务边界和多代理协作原则；Astra Profile 只补充“在确有独立并行收益时明确 delegation trigger”这一模型 delta。

## 3. Claude Fable 5.1：小范围修改

用户：给 Fable 5.1 写 coding prompt，只改配置文件里的两处字段，不要整文件重写。

设计时使用 Core + `references/models/anthropic/claude-fable-5.1.md`。Profile 只补充在结果等价时优先 targeted edit；范围、验证和状态真实性仍由 Core 负责。

## 4. Grok 4.6：Core-only

用户：给 Grok 4.6 写一个研究 prompt。

当前没有需要改变自然语言 Prompt 写法的 Grok 4.6 Profile，因此只使用 Core。不要为了模型支持列表完整而补充“Grok 风格”、Markdown、testing 或 delegation 等占位规则。

## 5. API 请求：按需加载

只有用户明确要求“给我 GPT-6 Structured Outputs 的请求体/SDK 配置”时，才额外加载 `references/api/openai.md`。合成 API 示例见 [openai-extraction-request.json](api/openai-extraction-request.json)。它不是普通 Prompt 任务的默认模板。
