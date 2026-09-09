# DeepSeek API Reference

Status: official-source verified 2026-09-09

**Cold-load rule:** only load for DeepSeek API/SDK requests, thinking configuration, sampling behavior, tool-loop state, JSON output, model IDs or protocol migration. Ordinary prompt work should use the DeepSeek V4 model Profile without this file.

## Official sources

- https://api-docs.deepseek.com/guides/thinking_mode/
- https://api-docs.deepseek.com/api/create-response/
- https://api-docs.deepseek.com/api/create-chat-completion/
- https://api-docs.deepseek.com/quick_start/pricing/
- https://api-docs.deepseek.com/updates/

## V4 models and thinking

- Official V4 IDs include `deepseek-v4-pro` and `deepseek-v4-flash`, with additional experimental variants documented separately.
- V4 thinking is currently enabled by default and the default effort is `high`.
- Native effort is primarily `low`, `high`, `max`; compatibility inputs such as `medium` and `xhigh` can map to `high`, with additional mappings in compatibility interfaces.
- In thinking mode, `temperature`, `top_p`, `presence_penalty` and `frequency_penalty` do not affect generation even when accepted for compatibility.

## Tool-loop state

- With thinking + tools, historical `reasoning_content` must be preserved and returned correctly on subsequent requests; missing required state can cause API errors.
- Without tools, the same state has different handling and should follow the current interface documentation.
- `reasoning_content` is protocol state. Do not ask the model to manage it through natural-language prompt text.

## Interfaces and output

- Current V4 Pro/Flash service documents 1M context and compatibility across DeepSeek Responses/Chat interfaces plus documented compatibility layers.
- JSON Output and Tool Calls have DeepSeek-specific semantics. Do not assume OpenAI Structured Outputs schema behavior solely because an interface is compatible.

## Migration boundary

When migrating old `deepseek-chat` / `deepseek-reasoner` integrations, verify current model IDs, thinking defaults, effort mappings, sampling behavior and tool-loop state rather than performing a string-only model replacement.

## Prompt boundary

Keep task instructions, scope and output behavior in the Prompt. Keep thinking switches, effort mapping, sampling no-ops, `reasoning_content`, endpoints and JSON/tool protocol here.
