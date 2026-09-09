# Model Profile: Claude Fable 5.1

Status: verified against Anthropic official docs on 2026-09-09.

## Official sources

- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- https://platform.claude.com/docs/en/models/fable-5-1/overview

## Relationship to Fable 5

Anthropic says existing Fable 5 prompts should generally work well on Fable 5.1. Start with the Core and Fable 5 principles, then add only 5.1 differences that match the task or observed failure.

## Prompt-relevant differences

- At low effort, Fable 5.1 may call search/retrieval tools less often; current-fact workflows can need an explicit search trigger.
- Prose can be denser than Fable 5, while 5.1 may use less structure by default. Do not carry aggressive anti-Markdown workarounds forward automatically.
- It can sometimes add nearby fixes, extensions or more permanent tests than requested; explicit scope/test boundaries reduce extras.
- Small edits may become whole-file rewrites; targeted-edit guidance can reduce unnecessary changes and latency.
- Independent tool calls can benefit from batching; the lead agent can continue useful work while subagents run when the harness supports that pattern.
- Long tasks can end early or ask permission again for already-authorized reversible work; explicit completion language can help when this failure appears.

## Prompt adaptations

Use only for the corresponding failure:

- **Dense prose**: request literal/direct language and enough paragraphing; avoid giant style blacklists.
- **Under-search at low effort**: for current/external facts, explicitly require use of actually available search/retrieval tools.
- **Scope creep**: do not fix unrelated behavior unless it blocks the requested result; report it as follow-up.
- **Excess permanent tests**: keep committed tests proportional to repository convention and requested behavior.
- **Whole-file rewrites**: prefer surgical edits when they achieve the same end result.
- **Premature stopping**: authorized reversible work should finish the requested scope rather than end on a plan or repeated permission request.

## API boundary

Effort values, preserved thinking, append-only history, compaction and other Anthropic integration mechanics live in [Anthropic API reference](../../api/anthropic.md). They are cold-loaded only for API/SDK tasks.

## Do not generalize

Do not copy these Fable 5.1-specific behaviors into Core or other model Profiles without evidence:

- low-effort under-search,
- formatting density/structure tendency,
- targeted-edit tendency,
- Fable-specific scope/test behavior,
- Anthropic history/thinking semantics.
