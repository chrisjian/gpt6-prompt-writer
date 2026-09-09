# GPT‑5.6 Family Profile

Status: official-source verified 2026-09-09

本 Profile 面向 GPT‑5.6 family。Sol / Terra / Luna 只保留会影响任务选择或 Prompt 设计的差异；没有证据时不为每个 SKU 复制完整方法论。

## Official sources

- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://developers.openai.com/api/docs/models/gpt-5.6-luna
- https://developers.openai.com/api/docs/guides/latest-model

## Prompt-relevant behaviors / facts

- Sol 定位复杂专业工作旗舰；Terra 平衡能力与成本；Luna 面向成本敏感、高吞吐工作负载。
- OpenAI 的 GPT‑6 Astra guidance 会把 Astra 与 GPT‑5.6 Sol 等前代作行为对比，因此 Astra-specific prompting workaround 不能默认下沉到 GPT‑5.6 family。
- 当前没有足够官方依据说明 Sol / Terra / Luna 需要三套完全不同的自然语言 Prompt 方法。

## Prompt adaptations

- 先应用通用 Core；只有官方资料或真实 eval 证明行为差异时才加入 GPT‑5.6-specific 规则。
- 明确 Sol/Terra/Luna 时保留 variant，但不要把成本/吞吐定位转化为降低事实边界、验收标准或任务约束。
- 从 GPT‑6 Astra prompt 迁回 GPT‑5.6 时，逐项审计 Astra 专属的 initiative、格式、Skills/AGENTS、delegation、验证等规则，不原样继承。

## Variant notes

### Sol
复杂专业工作、质量优先场景。

### Terra
能力/成本平衡；目前作为 family variant，而不是另一套 Prompt Core。

### Luna
高吞吐/成本敏感场景。成本定位不等于可以删除必要的质量约束。

## API boundary

Alias、精确 model ID、reasoning-effort 值、context/output、工具能力和可运行迁移参数见 [OpenAI API reference](../../api/openai.md)。普通 Prompt 任务不加载该文件。

## Do not generalize

- 不把 GPT‑6 Astra 的格式、澄清、delegation、验证倾向当成 GPT‑5.6 family 事实。
- 不声称 Sol、Terra、Luna 需要完全不同的 Prompt 写法，除非后续官方资料或 eval 证明。
- 不从 API 参数差异反推出未经验证的自然语言行为差异。
