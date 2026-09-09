# Doubao Seed 2.x Family Profile

Status: thin official-source profile verified 2026-09-09

本 Profile 面向 Doubao Seed 2.x family。当前缺少与 OpenAI/Anthropic/Google 同等级的通用文本 Prompting Guide，因此刻意保持薄，只保留模型定位和可靠的 Prompt 边界。

## Official sources

- https://developer.volcengine.com/articles/7610285824933445675
- https://developer.volcengine.com/articles/7636596381943070763
- https://developer.volcengine.com/articles/7615528054736945158

## Prompt-relevant behaviors / facts

- Seed 2.x family 包含 Pro、Lite、Mini 与 Code 等定位：Pro 偏复杂推理/Agent，Lite 偏均衡与性价比，Mini 偏速度/成本，Code 偏真实编程/IDE/Skills 场景。
- 这些产品定位不足以推出固定 Markdown、verbosity、clarification、testing 或 delegation 倾向。
- Code variant 的 coding/Skills 定位不意味着任意接入都自动拥有同一套 IDE/harness 工具。

## Prompt adaptations

- 使用通用 Core 作为主要 Prompt 方法，不发明“豆包专属文风模板”。
- 根据任务复杂度、成本、吞吐和 coding 场景选择 variant，但不因为 Lite/Mini 更便宜就删除必要事实边界或验收标准。
- Agent/Coding Prompt 只依赖宿主真实提供的 Skills、browser/computer/tool 能力；产品定位不是工具开关。
- 如果任务要求某个 harness 的 rules/skills/subagents/hooks/permissions，实时核验该 harness，而不是把宿主机制固化进本 Model Profile。

## Variant notes

### Pro
复杂推理、Agent、高难度任务。

### Lite
均衡/性价比。

### Mini
速度、成本优先。

### Code
Coding/IDE/Skills 场景优化；不代表所有 API 或 harness 具有相同工具。

## API boundary

Coding Plan/在线推理接入、endpoint/model name、thinking/reasoning 配置、版本迁移和具体工具能力见 [Volcengine / Doubao API reference](../../api/volcengine.md)。普通 Prompt 任务不加载该文件。

## Do not generalize

- 不臆造 Doubao 的 Markdown、verbosity、clarification、testing、delegation 默认倾向。
- 不把营销 benchmark 当 Prompting Guide。
- 不把 Code variant 的 harness 能力假定给整个 Seed 2.x family。
