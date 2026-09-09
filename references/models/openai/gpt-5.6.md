# GPT‑5.6 Family Profile

Status: official-source verified 2026-09-09

本 Profile 面向 GPT‑5.6 family。共性只写一次，Sol / Terra / Luna 仅保留 variant 差异；除非官方资料或可重复 eval 证明行为确实不同，不为每个 SKU 复制完整 Prompt 规则。

## Official sources

- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://developers.openai.com/api/docs/models/gpt-5.6-luna
- https://developers.openai.com/api/docs/guides/latest-model

## Verified model behaviors / facts

- Family 包含 GPT‑5.6 Sol、Terra、Luna；`gpt-5.6` alias 指向 Sol。
- 三个主要 variant 均支持 reasoning effort `none / low / medium / high / xhigh / max`；当前模型页默认 `medium`。
- Sol 定位复杂专业工作旗舰；Terra 平衡能力与成本；Luna 面向成本敏感、高吞吐工作负载。
- 当前官方模型表显示它们共享 1.05M context、128K max output，并支持 Functions、Web search、File search、Computer use。
- GPT‑6 Astra 官方 guidance 会把 Astra 与 GPT‑5.6 Sol 等前代作行为对比，因此 Astra-specific workaround 不能默认下沉到 5.6 family。

## Prompt adaptations

- 先应用通用 Core；只有 GPT‑5.6 官方资料或实际 eval 能证明差异时才加入 family-specific 行为规则。
- 用户只说 `GPT-5.6` 时按 Sol 处理；明确 Sol/Terra/Luna 时保留 variant。
- 不把“Sol 更强 / Luna 更便宜”转化成不同写作模板。variant 主要影响模型选择、预算、吞吐和 reasoning 配置。
- 从 GPT‑6 Astra prompt 迁回 GPT‑5.6 时，审计 Astra 专属的 initiative、格式、Skills/AGENTS、验证等 workaround，不能直接继承。

## API / runtime notes

- `gpt-5.6-sol`；alias `gpt-5.6`。
- `gpt-5.6-terra`。
- `gpt-5.6-luna`。
- API 参数与支持能力要求“最新/可运行”时重新核验 OpenAI 官方模型页。

## Variant notes

### Sol
复杂专业工作优先；适合质量优先且任务复杂的场景。

### Terra
能力/成本平衡；作为 family variant，而不是另写一套 Prompt Core。

### Luna
成本敏感、高吞吐场景优先。不要仅因 Luna 更快/更便宜就自动删除必要约束或验收标准。

## Migration notes

- 从旧 GPT‑5.x 迁移时，先核验 model ID、reasoning effort 与宿主能力。
- 从 GPT‑6 Astra 迁移时，把 Astra Profile 当“待审计来源”而不是默认兼容层。

## Do not generalize

- 不把 GPT‑6 Astra 的格式、澄清、delegation、验证倾向当成 GPT‑5.6 family 事实。
- 不声称 Sol、Terra、Luna 需要完全不同的 Prompt 写法，除非后续官方资料或 eval 证明。
- 不默认更高 reasoning effort 一定更好。
