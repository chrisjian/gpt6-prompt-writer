# Anthropic API Reference

Status: official-source verified 2026-09-09

**Cold-load rule:** only load this file for Anthropic API/SDK configuration, effort selection, thinking/history state, compaction or other programmatic integration questions. Ordinary prompt work should use the Fable model Profiles without this file.

## Official sources

- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
- https://platform.claude.com/docs/en/models/fable-5-1/overview

## Effort

- Anthropic describes effort as the main intelligence/latency/cost control for Fable 5-family workloads.
- For Fable 5, current guidance uses `high` as a default starting point for many tasks, with higher/lower levels evaluated against the workload rather than assumed better.
- For Fable 5.1, re-evaluate all effort levels on the target task; same-named effort levels do not imply the same amount of thinking across model generations.
- Effort selection is configuration. Its prompt implication—such as constraining scope when high effort over-deliberates—belongs in the model Profile.

## Thinking and conversation state

- Thinking visibility and preserved thinking blocks depend on the supported Anthropic API/harness mechanisms; do not request private chain-of-thought as ordinary response text.
- Fable 5.1 has stricter considerations around preserved thinking and append-only conversation histories. Editing earlier turns can invalidate the expected state/caching behavior.
- Compaction, tool batching, progress-update mechanisms and long-running state are runtime/API features, not abilities created by prompt wording.

## Integration boundary

- Host-managed subagents, memory, async communication and UI progress mechanisms are not guaranteed by the model API alone.
- When runnable integration details are requested, verify the current Anthropic API/model docs for the exact endpoint and supported fields.

## Prompt boundary

Keep model-visible instructions focused on task, scope, completion, style and tool-use behavior. Keep effort values, thinking/history protocol and state-management mechanics in the API/harness configuration.
