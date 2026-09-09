# OpenAI API Reference

Status: official-source verified 2026-09-09

## Official sources

- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/guides/latest-model
- https://developers.openai.com/api/docs/models/gpt-6-astra
- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://developers.openai.com/api/docs/models/gpt-5.6-luna

## GPT-6 Astra

- Model ID: `gpt-6-astra`.
- Current reasoning efforts: `low`, `medium`, `high`, `xhigh`, `max`; `none` is not supported.
- Context window: 1,050,000 tokens. Max output: 128,000 tokens.
- Tool calling with GPT-6 Astra requires the Responses API; Chat Completions is otherwise supported.
- When migrating from `none` or `minimal`, OpenAI recommends starting with `low` and comparing results. Otherwise preserve the current effective effort unless evals justify a change.
- Remove unsupported sampling/logprob parameters listed in current guidance rather than encoding them as prompt text.
- Structured Outputs, prompt caching, compaction, persisted reasoning, computer use and related capabilities are API/harness features, not prompt switches.

## GPT-5.6 family

- `gpt-5.6` is the Sol alias; explicit family IDs include `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`.
- Current family model pages expose reasoning efforts `none`, `low`, `medium`, `high`, `xhigh`, `max`; current default is `medium`.
- Current family pages show 1.05M context and 128K max output, with Functions, Web search, File search and Computer use support. Recheck the specific variant before producing runnable configuration.
- Sol, Terra and Luna primarily differ in capability/cost/throughput positioning; do not infer different natural-language prompt methods from the SKU alone.

## Migration boundary

- Protocol compatibility does not imply model-behavior equivalence.
- Keep model-behavior adaptations in `references/models/openai/`; keep IDs, parameter values, protocol and capability matrices here.
- When the user asks for current runnable code, reopen the official model/API documentation rather than treating this snapshot as permanent.

## Prompt boundary

Do not copy API fields into the model-visible prompt and claim they configure reasoning, tools, structured output, caching or context. Prompt wording controls behavior within capabilities that the API/harness has actually enabled.
