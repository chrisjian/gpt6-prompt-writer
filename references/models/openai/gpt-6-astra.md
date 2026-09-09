# Model Profile: GPT‑6 Astra

Status: verified against current OpenAI docs on 2026-09-09.

## Official sources

- Model guidance: https://developers.openai.com/api/docs/guides/latest-model
- Model page: https://developers.openai.com/api/docs/models/gpt-6-astra

## Prompt-relevant behaviors

OpenAI currently highlights five areas that can materially change GPT‑6 Astra prompt design:

1. **Initiative and follow-through**: Astra may ask focused questions when missing information changes the result; authorized reversible work should bias toward action rather than repeated approval pauses.
2. **Instruction following**: Astra follows instructions strongly and can be especially sensitive to Skills, `AGENTS.md`, and other instruction files. Silent or conflicting guidance should be audited.
3. **Personality and writing style**: Astra tends toward detailed, formatted responses and recurring phrasing. Specify the desired style/structure when this matters.
4. **Subagent delegation**: Astra may delegate less than some harnesses want. Tune delegation only when the actual harness provides subagents and parallelism is useful.
5. **Testing and verification**: Astra can over-verify coding work. Calibrate verification to the change and stop broadening after required checks pass unless new failures or risks justify more.

## Prompt adaptations

Use the Core first. Add only the Astra-specific controls needed by the task:

- For unnecessary confirmation: state authorized reversible scope, true blockers and completion conditions.
- For Skill/AGENTS conflicts: identify the actual instruction source and preserve the real priority order.
- For over-formatting: request clear prose and use lists/tables only where structure genuinely helps.
- For under-delegation: define when parallel subagents are useful; do not force delegation for tiny or sequential work.
- For over-testing: require project checks and affected-behavior verification; repeat or broaden only on new changes, failures or unresolved concerns.

## API boundary

Model IDs, reasoning-effort values, context/output limits, Responses/tool-calling requirements, Structured Outputs, caching/compaction and migration parameters are cold-loaded from [OpenAI API reference](../../api/openai.md). Ordinary prompt work does not load that file.

## Prompt migration notes

When migrating older prompts to Astra, audit repeated approval rules, long prescriptive Skill/AGENTS instructions, forced repeated testing and fixed formatting workarounds. Keep only rules that still correspond to the task, a current Astra failure mode or a harness requirement.

## Do not generalize

Do not copy these Astra-specific behaviors into other model profiles without evidence:

- detailed/Markdown-heavy output tendency,
- over-verification tendency,
- possible under-delegation relative to a multi-agent harness,
- Astra-specific initiative/clarification behavior,
- OpenAI API configuration (which belongs in the API reference, not another model Profile).
