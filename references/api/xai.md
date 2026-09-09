# xAI API Reference

Status: official-source verified 2026-09-09

## Official sources

- https://docs.x.ai/developers/grok-4-6
- https://docs.x.ai/developers/models
- https://docs.x.ai/developers/advanced-api-usage/prompt-caching
- https://docs.x.ai/developers/advanced-api-usage/context-compaction

## Grok 4.6 configuration

- Model ID: `grok-4.6`.
- Current reasoning efforts: `low`, `medium`, `high` (default), `xhigh`.
- Context window: 500,000 tokens.
- Supported interfaces include Responses API and Chat Completions.
- Official tool capabilities include function calling, Web Search, X Search and code execution when enabled through the selected interface/harness.

## Current information

Grok does not obtain realtime/current-event information merely because a prompt asks for it. The integration must enable an appropriate search tool, and the task must actually use that tool.

## Caching and compaction

- xAI recommends `prompt_cache_key` for Responses API or `x-grok-conv-id` for Chat Completions to improve cache affinity.
- Stable prompt/message prefixes improve cache reuse.
- For long tool-heavy loops, xAI documents context compaction to reduce stale context and cost.

## Prompt boundary

Search availability, reasoning level, cache keys and compaction are API/harness configuration. Grok 4.6 otherwise uses the model-neutral Core unless a future prompt-specific delta justifies a Profile.
