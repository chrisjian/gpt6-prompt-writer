# 跨模型提示词工程参考

本文件记录从其他前沿模型官方提示词指南中吸收的**通用工程启发**。这些内容用于改进本项目的提示词设计方法，不代表 OpenAI 对 GPT‑6 Astra 的官方要求。GPT‑6 的模型事实与官方行为建议仍以 `gpt6-best-practices.md` 和 OpenAI 当前文档为准。

核验日期：**2026-09-09**。

## 参考来源

- Anthropic: [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)
- Anthropic: [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)

## 吸收为项目工程原则

### 1. 根因级指令优先

当多个失败表现可以由同一个行为原则解释时，优先写一条明确的正向规则，而不是分别枚举每个症状和禁令。

项目落地：Prompt Audit 会合并同根因规则；compression 优先减少 instruction surface area，而不是只减少字符数。

### 2. Purpose / Why 条件化加入

任务用途只有在会改变信息筛选、优先级、风险权衡或输出结构时才进入任务契约。无决策价值的背景不因为“更完整”而保留。

项目落地：最小任务契约把用途设为可选字段，不要求所有提示词都写背景段。

### 3. 状态声明不可越级

计划、推断、意图不能升级成“已读取、已搜索、已修改、已验证、已通过、已完成”。状态应由实际输入、工具结果或可检查产物支持。

项目落地：默认只报告必要状态，不要求附完整日志或原始证据；用户要求审计、复现或核查时再展开。

### 4. 简洁靠内容选择，不靠电报体

简洁优先通过删除不会影响理解、判断或行动的信息实现，而不是把完整表达压成碎片句、过度缩写、符号链或难读术语。

项目落地：区分 instruction compression 与 output concision；两者都不等于机械缩短句子。

### 5. 先判断意图类型，再应用自主执行

分析、建议和执行是不同交付模式。问题描述不自动授权修改；明确行动请求也不应被降级为能力确认或只给计划。

项目落地：自主性建立在真实用户意图和授权范围之上。

### 6. 微妙行为用代表性正例定界

当文字规则已经清楚，但某种风格、格式或边界行为仍容易被误解时，一个小而代表性的正确示例通常比继续增加多个近义禁令更有效。

项目落地：示例按失败添加；简单任务和稳定行为不默认 few-shot。

## 不迁移为 GPT‑6 通用规则

以下内容可能对 Fable 5 / 5.1 有模型特定价值，但没有足够依据写入 GPT‑6 Core：

- Fable 5 / 5.1 自身的 Markdown、标题、列表等默认格式倾向。
- Anthropic 对具体 effort 档位的推荐起点。
- 某个 effort 档位下需要额外 search nudge 的模型特性。
- 固定每 N 步自检、固定周期 verifier 或其他长程 Agent 编排策略。
- Claude 专属 API、工具调用或运行时参数。

如果未来 OpenAI 官方 GPT‑6 指南出现同类建议，应以新的 GPT‑6 一手资料重新评估，而不是因为其他模型采用了该策略就自动迁移。
