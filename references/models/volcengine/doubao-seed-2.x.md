# Doubao Seed 2.x Family Profile

Status: thin official-source profile verified 2026-09-09

本 Profile 面向 Doubao Seed 2.x family。当前官方资料足以支持模型定位、thinking/Agent/Coding 等 runtime 适配，但尚缺少与 OpenAI/Anthropic/Google 同等级的通用文本 Prompting Guide，因此刻意保持“薄 Profile”。

## Official sources

- https://developer.volcengine.com/articles/7610285824933445675
- https://developer.volcengine.com/articles/7636596381943070763
- https://developer.volcengine.com/articles/7615528054736945158
- 火山方舟对应模型页与 API 控制台文档（交付可运行配置时重新核验）

## Verified model behaviors / facts

- Doubao Seed 2.0 family 包含 Pro、Lite、Mini 三款通用模型及 Code variant。
- Pro 定位复杂推理 / Agent；Lite 强调性价比并持续增强 Agent/Coding/全模态能力；Mini 优先速度/成本；Code 针对真实编程环境、Claude Code/Skills 等工具环境优化。
- 官方 Coding Plan 与在线推理 API 的 Base URL、Model Name、计费方式不同，不能混用。
- 官方资料显示 Seed 2.x family 支持 thinking / reasoning-effort 类能力的具体范围会随型号与版本更新；交付参数时必须按当前模型页核验。
- 新版 Lite/Mini 强调长任务、Agent、GUI/多模态等能力，但这些产品描述不足以推出固定 Markdown、澄清、验证或文风倾向。

## Prompt adaptations

- 使用通用 Core 作为主要 Prompt 方法，不额外发明“豆包专属文风模板”。
- 根据任务选择 Pro/Lite/Mini/Code：复杂 Agent → Pro；高频成本敏感 → Lite/Mini；Coding/IDE harness → Code；具体选择仍以用户约束和当前模型版本为准。
- Agent/Coding 场景只描述宿主真实提供的 Skills、browser/computer/tool 能力；产品宣传中的能力不等于当前接入一定已启用。
- Coding Plan 调用优先核验 Coding Plan model name/base URL；在线推理则使用对应 endpoint/model ID。
- thinking 与 reasoning 参数只作为 runtime 配置，不把“深度思考”文字重复塞进 Prompt 当作替代。

## API / runtime notes

- Coding Plan 与在线推理是不同接入面；不要混淆 endpoint/model name。
- 不在本 Profile 固化 Seed 2.1 或后续版本的 reasoning 枚举，除非用户指定该版本并实时核验。
- 多模态/GUI/Computer Use 能力按具体型号和宿主核验。

## Variant notes

### Pro
复杂推理、Agent、高难度任务。

### Lite
均衡/性价比；新版本持续增强全模态与 Agent/Coding。

### Mini
速度、成本优先。

### Code
Coding/IDE/Skills 场景优化；不表示任意 API endpoint 都自动拥有完整 IDE 工具。

## Migration notes

- Seed 2.0 → 2.1 或更新版本时优先重新核验 model ID、thinking/effort 枚举与 conversation state。
- Coding Plan ↔ 在线推理迁移时必须重新核验 endpoint、model name 与计费接口。

## Do not generalize

- 不臆造 Doubao 的 Markdown、verbosity、clarification、testing、delegation 默认倾向。
- 不把社区文章或营销 benchmark 当成 Prompting Guide。
- 不因为 Code variant 支持 Skills 就假定所有 Seed 2.x variant 都具有相同 harness 行为。
