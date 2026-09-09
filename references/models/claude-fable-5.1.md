# Model Profile: Claude Fable 5.1

Status: verified against Anthropic official docs on 2026-09-09.

## Official sources

- Prompting Claude Fable 5.1: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
- Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Model overview: https://platform.claude.com/docs/en/models/fable-5-1/overview

## Relationship to Fable 5

Anthropic says existing Fable 5 prompts should generally work well on Fable 5.1. Start with the Fable 5 Profile plus the Core, then add only the 5.1 differences that match observed behavior.

## Verified model differences

Anthropic currently calls out these 5.1-specific areas:

- Re-evaluate all effort levels; `high` remains the documented default starting point, but effort labels do not represent identical thinking amounts across model generations.
- At `low` effort, Fable 5.1 may call search/retrieval tools less often; current-fact workflows can need an explicit search trigger.
- Prose can be denser than Fable 5, while Fable 5.1 may use less structure/formatting by default. Do not carry aggressive anti-Markdown workarounds forward automatically.
- It can sometimes add nearby fixes, extensions, or more persistent test files than the task asks for; explicit scope/test boundaries reduce extras.
- Small edits may be implemented as whole-file rewrites; targeted-edit guidance can reduce unnecessary output and latency.
- Agent loops can benefit from batching independent tool calls, while the lead agent should keep working when useful subagents run.
- Conversation-history handling has stricter runtime considerations around preserved thinking and append-only histories; this is a harness concern, not a prose-style rule.
- Long tasks can end before the requested work is complete or ask permission for already-authorized work; explicit finish-the-whole-task language can help when this failure is observed.

## Prompt adaptations

Use only when the corresponding failure is present:

- **Dense prose**: ask for literal, direct language and enough paragraphing; do not automatically add a large style blacklist.
- **Under-search at low effort**: for current or externally verifiable facts, explicitly require use of the available search/retrieval tools before answering from memory.
- **Scope creep**: say not to fix or extend unrelated behavior unless it blocks the requested result; report unrelated findings as follow-up items.
- **Excess permanent tests**: keep committed tests proportional to repository convention and stated behavior; scratch checks need not become permanent files.
- **Whole-file rewrites**: prefer surgical edits when they produce the same end result and the file is not mostly changing.
- **Premature stopping**: when the task is clearly authorized and reversible, require completion rather than ending on a plan or asking permission again.

## Effort

Anthropic recommends starting at `high` and evaluating `low`, `medium`, `xhigh`, and `max` on the actual task. Do not infer that a same-named effort level is equivalent to Fable 5 or another model.

## Runtime notes

For API/harness integrations, preserve conversation state according to current Anthropic guidance. Thinking-block replay, append-only history, compaction, tool batching, and progress updates are runtime behaviors and must not be faked with prompt text.

## Do not generalize

Do not copy these Fable 5.1-specific behaviors into Core or other model profiles without evidence:

- low-effort under-search,
- Fable 5.1 formatting density/structure tendency,
- targeted-edit tendency,
- Anthropic thinking/history constraints,
- Fable 5.1 effort defaults and values,
- model-specific safeguard/refusal workarounds.
