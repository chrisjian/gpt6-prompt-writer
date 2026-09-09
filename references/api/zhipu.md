# Zhipu GLM API Reference

Status: official-source verified 2026-09-09

## Official sources

- https://docs.bigmodel.cn/cn/guide/models/text/glm-5
- https://docs.bigmodel.cn/cn/guide/models/text/glm-5.2
- https://docs.bigmodel.cn/cn/guide/capabilities/thinking
- https://docs.bigmodel.cn/cn/guide/capabilities/thinking-mode
- https://docs.bigmodel.cn/cn/guide/start/migrate-to-glm-new

## Version-sensitive limits

- GLM-5 official material documents a 200K context window.
- GLM-5.2 official material documents 1M context and 128K max output.
- Do not apply GLM-5.2 limits or parameters to GLM-5/5.1 without checking the exact model version.

## Thinking

- GLM-5.x models currently default to thinking enabled; earlier GLM versions can have different defaults.
- Interleaved thinking is supported from the documented 4.5-era capability onward and affects tool-loop state handling.
- `reasoning_effort` is currently documented for GLM-5.2+ rather than the entire 5.x family.
- Current mappings document `none/minimal` as no thinking, `low/medium` mapping to `high`, and `xhigh` mapping to `max`, with `max` recommended by the current 5.2 guidance. Recheck before runnable configuration.

## Tool-loop state

Reasoning content and tool results must be preserved/assembled according to the current API protocol for interleaved thinking. This is conversation state, not model-visible prompt content.

## Other capabilities

Function Calling, structured output and context caching are version/interface capabilities. Sampling migration guidance such as `temperature`/`top_p` should be checked against the target version's current migration page.

## Prompt boundary

GLM 5.x uses the model-neutral Core for natural-language Prompt design. Context limits, thinking switches, effort mappings, reasoning state and API feature fields belong here.
