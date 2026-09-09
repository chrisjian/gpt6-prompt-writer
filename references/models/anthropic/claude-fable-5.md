# Model Profile: Claude Fable 5

Status: verified against Anthropic official docs on 2026-09-09.

## Official sources

- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

## Prompt-relevant behaviors

- Stronger instruction following means one concise root-cause instruction can often replace many symptom-level prohibitions.
- Hard tasks can run substantially longer; more deliberative configurations can encourage unrequested cleanup or abstraction unless scope is explicit.
- Long autonomous runs benefit from grounding progress/completion claims in actual tool results.
- The model can occasionally act when the user was only assessing a problem; explicit analysis-vs-action boundaries help.
- Purpose/audience context can materially improve prioritization when it changes how the task should be approached.
- Long-run final messages can become dense or rely on internal shorthand; user-facing summaries should re-ground the reader.
- Skills/prompts designed for older models may be too prescriptive and should be re-evaluated instead of automatically preserved.

## Prompt adaptations

Use the Core first. Add Fable 5-specific guidance only when relevant:

- Prefer one concise root-cause instruction over many near-duplicate prohibitions.
- For long autonomous tasks, require truthful status claims tied to actual results, without forcing raw logs into the final answer.
- Separate assessment from state-changing action; explicit action requests proceed within scope.
- When the task is vulnerable to cleanup/refactoring/defensive extras, make scope boundaries explicit.
- For long user-facing summaries, request outcome-first complete sentences and remove working shorthand.
- Re-test old Skills/system prompts and remove legacy scaffolding that no longer improves actual results.

## API boundary

Effort selection, thinking visibility, preserved thinking/history, compaction and other Anthropic integration mechanics live in [Anthropic API reference](../../api/anthropic.md). Ordinary Prompt work does not load that file.

## Do not generalize

Do not automatically transfer these Fable 5 specifics to other models:

- Fable-specific long-run/scope behavior,
- Anthropic effort or thinking semantics,
- fresh-context verifier or periodic self-verification patterns,
- Claude memory/subagent/tooling conventions.
