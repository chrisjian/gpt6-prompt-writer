# Google Gemini API Reference

Status: official-source verified 2026-09-09

## Official sources

- https://ai.google.dev/gemini-api/docs/gemini-3
- https://ai.google.dev/gemini-api/docs/models

## Thinking and sampling

- Gemini 3 uses dynamic thinking; `thinking_level` controls maximum thinking depth and current official guidance defaults it to `high`.
- Google currently recommends keeping Gemini 3 temperature at the default `1.0`; lowering it can cause looping or reduced performance on complex reasoning tasks.
- OpenAI-compatible reasoning effort may be mapped to Gemini-native thinking levels. Treat that as compatibility-layer behavior, not cross-vendor semantic equivalence.

## Conversation state

- Stateful Interactions API can manage thought signatures automatically.
- When manually constructing stateless conversation history, preserve the required thought blocks/signatures according to current Gemini API guidance.
- Thought signatures are protocol state; never turn them into natural-language instructions for the model.

## Tools and model limits

- Gemini 3 supports built-in tools and function calling combinations subject to the specific model/interface.
- Computer Use support, context limits, output limits, preview/stable status and per-model tool availability can change; check the current Models page before producing runnable configuration.

## Migration boundary

- The prompt-level recommendation to remove old chain-of-thought forcing belongs in Core unless a model-specific delta is still needed.
- `thinking_level`, temperature and thought-signature management belong here.

## Prompt boundary

Do not claim a prompt string configures `thinking_level`, sampling, thought signatures or tool availability. These must be set through the actual API/harness.
