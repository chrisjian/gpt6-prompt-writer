# Model Profile: Claude Fable 5

Status: verified against Anthropic official docs on 2026-09-09.

## Official sources

- Prompting Claude Fable 5: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

## Verified model behaviors

Anthropic documents these Fable 5 behaviors as particularly relevant to prompting and scaffolding:

- Stronger instruction following means many behaviors can be steered with a brief instruction instead of enumerating every symptom.
- Hard tasks can run substantially longer, especially at higher effort.
- Higher effort can over-deliberate on routine tasks and can encourage unrequested cleanup or abstraction unless scope is explicit.
- Long autonomous runs benefit from grounding progress/completion claims in actual tool results.
- The model can occasionally take unrequested actions when the user was only describing or assessing a problem; explicit scope boundaries help.
- Anthropic recommends giving the reason behind a request when that context changes how the task should be approached.
- Long-run final messages can become dense or rely on working shorthand; user-facing summaries should re-ground the reader and favor clarity over compression.
- Skills and prompts designed for older models may be too prescriptive and should be re-evaluated instead of automatically preserved.

## Prompt adaptations

Use the Core first. Add Fable 5-specific guidance only when relevant:

- Prefer one concise root-cause instruction over many symptom-level prohibitions.
- For long autonomous tasks, require truthful status reporting tied to actual tool results, but do not force raw logs into the final answer.
- When the user is asking for assessment rather than change, stop at the assessment; when change is explicitly requested, proceed within scope.
- At higher effort, add explicit scope discipline if the task is vulnerable to cleanup, refactoring, defensive extras, or speculative abstractions.
- For long user-facing summaries, request outcome-first complete sentences and drop internal shorthand.
- Re-test old Skills/system prompts and remove legacy scaffolding that no longer improves eval results.

## Effort

Anthropic describes effort as the main intelligence/latency/cost control for Fable 5 and recommends `high` as a default starting point for most tasks, with `xhigh` for capability-sensitive work and `medium`/`low` for routine work. Treat this as Fable-specific configuration guidance and validate against real workloads.

## Runtime notes

Long-running behavior, memory systems, subagents, async communication, progress tools, and thinking visibility depend on the host/API. Prompt text alone does not create them.

Anthropic also warns against asking the model to reproduce internal reasoning as response text; use supported thinking/progress mechanisms instead when the application needs visibility.

## Do not generalize

Do not automatically transfer these Fable 5 specifics to other models:

- `high` as the default effort starting point,
- Anthropic-specific long-run scaffolding,
- Fable safety/refusal behavior,
- fresh-context verifier or periodic self-verification recommendations,
- Claude thinking blocks, memory conventions, or send-to-user tooling.
