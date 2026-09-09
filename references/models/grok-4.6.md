# Model Profile: Grok 4.6

Status: verified against current xAI official docs on 2026-09-09. Prompt-style guidance is intentionally conservative because xAI currently documents the model/API in more detail than general text-prompt behavioral tendencies.

## Official sources

- Grok 4.6: https://docs.x.ai/developers/grok-4-6
- Models: https://docs.x.ai/developers/models
- Prompt caching: https://docs.x.ai/developers/advanced-api-usage/prompt-caching
- Context compaction: https://docs.x.ai/developers/advanced-api-usage/context-compaction
- Grok Build: https://docs.x.ai/build/overview

## Verified model/API facts

- Model ID: `grok-4.6`.
- xAI currently lists reasoning efforts `low`, `medium`, `high` (default), and `xhigh`.
- Context window: 500,000 tokens.
- APIs: Responses API and Chat Completions.
- Official tool capabilities include function calling, web search, X search, and code execution.
- Grok does not have realtime/current-event knowledge beyond its training data unless search tools are enabled and used.
- xAI recommends `prompt_cache_key` for Responses API or `x-grok-conv-id` for Chat Completions to improve cache affinity.
- Stable prompt/message prefixes improve cache hits. For long tool-heavy loops, xAI documents context compaction as a way to reduce stale context and cost.

## Prompt adaptations

Until xAI publishes or exposes a comparable general text-model prompting guide for Grok 4.6, use the model-neutral Core as the default and only add behavior rules justified by actual evals.

Safe current adaptations:

- For current facts, require use of enabled Web Search / X Search rather than treating model memory as realtime data.
- Do not claim tools exist unless the host/API actually enabled them.
- Keep static instructions/reference material stable when practical if the application benefits from prompt caching; this is a runtime optimization, not a reason to bloat the prompt.
- In long agent loops, consider host-supported compaction instead of repeatedly carrying stale verbose tool output.

## Reasoning

The current official model page lists `high` as the default reasoning level. Treat that as xAI-specific runtime configuration; do not encode it into generic prompt text and do not assume the same effort semantics as OpenAI or Anthropic.

## Grok Build

Grok Build uses Grok 4.6 by default and can load project/user instructions, skills, plugins, hooks, MCP servers, and custom models. When a prompt is intended for Grok Build, inspect the actual harness configuration before adding assumptions about available tools or instruction files.

## Do not generalize

Do not infer or export unverified Grok behaviors such as:

- a preferred prose/Markdown style,
- a tendency to over- or under-verify,
- a default delegation strategy,
- a particular clarification/autonomy tendency,
- OpenAI- or Anthropic-specific reasoning, history, structured-output, or Skill semantics.

Those require xAI documentation or reproducible Grok 4.6 eval evidence before entering this Profile.
