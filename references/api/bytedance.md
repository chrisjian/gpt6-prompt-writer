# ByteDance / Doubao API Reference

Status: official-source verified 2026-09-09

ByteDance Seed 是模型侧品牌/组织；当前主要开发者 serving/API 平台是 Volcengine / Ark（火山引擎/火山方舟）。目录按厂商统一使用 `bytedance`，但实际接入参数仍以 Volcengine/Ark 当前文档为准。

## Official sources

- https://developer.volcengine.com/articles/7610285824933445675
- https://developer.volcengine.com/articles/7636596381943070763
- https://developer.volcengine.com/articles/7615528054736945158
- Use the current Volcengine Ark model/API console documentation for runnable endpoint and model-name details.

## Integration surfaces

- Coding Plan and online inference are different integration surfaces with different Base URL / model-name / billing conventions. Do not mix their configuration.
- Seed 2.x model IDs, thinking/reasoning controls and supported capabilities can change by variant/version; verify the exact current model before returning runnable code.
- Multimodal, GUI and Computer Use/tool capabilities are also variant- and host-dependent.

## Coding Plan

The Code variant is positioned for coding/IDE/Skills workflows, but this does not mean every generic online inference endpoint automatically exposes the same harness tools or Coding Plan behavior.

## Migration boundary

- Seed 2.0 → later versions: recheck model ID, thinking/effort controls and conversation-state requirements.
- Coding Plan ↔ online inference: recheck endpoint, model name, authentication/billing surface and available tools.

## Prompt boundary

Doubao Seed 2.x uses the model-neutral Core for natural-language Prompt design. Endpoint/model-name details, thinking controls and tool availability belong here; prompt wording does not substitute for actual configuration.
