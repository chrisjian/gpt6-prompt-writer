# Model Profile: Grok 4.6

Status: verified against current xAI official docs on 2026-09-09. Prompt-style guidance is intentionally conservative because xAI currently documents API/runtime behavior more fully than general text-prompt tendencies.

## Official sources

- https://docs.x.ai/developers/grok-4-6
- https://docs.x.ai/developers/models
- https://docs.x.ai/build/overview

## Prompt-relevant behaviors / facts

- xAI currently provides limited official evidence for Grok 4.6-specific prose, Markdown, verification, delegation or clarification tendencies. Use the model-neutral Core unless reproducible eval evidence supports a Grok-specific rule.
- For current/realtime facts, the task must rely on an actually enabled search capability rather than treating model memory as realtime data.
- Tool availability depends on the real integration/harness; prompt wording cannot create search, code execution or other tools.

## Prompt adaptations

- Default to Core and avoid inventing a “Grok style” template.
- Current-fact prompts should explicitly require use of the available search source before asserting fresh facts.
- Do not import GPT/Claude-specific testing, Markdown, delegation or clarification workarounds without Grok evidence.
- If the prompt targets a harness such as Grok Build and depends on rules/skills/subagents/hooks/permissions, verify that harness’s current behavior at task time instead of maintaining those mechanics in this Model Profile.

## API boundary

Model ID, reasoning levels, context limit, Responses/Chat interfaces, search/tool configuration, prompt-cache fields and compaction are cold-loaded from [xAI API reference](../../api/xai.md).

## Do not generalize

Do not infer or export unverified Grok behaviors such as:

- a preferred prose/Markdown style,
- a tendency to over- or under-verify,
- a default delegation strategy,
- a particular clarification/autonomy tendency,
- another vendor’s reasoning/history/structured-output semantics.
