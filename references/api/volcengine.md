# Volcengine / Doubao API Reference

Status: official-source verified 2026-09-09

**Cold-load rule:** only load for Volcengine/Doubao API or Coding Plan setup, model names, endpoints, thinking/reasoning parameters, multimodal/tool capability or migration. Ordinary Doubao prompt work should use the thin model Profile without this file.

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

Variant positioning can influence model selection, but endpoint/model-name details, thinking controls and tool availability belong here. Do not repeat “deep thinking” phrases in the Prompt as a substitute for actual configuration.
