# Model Profile: GPT‑6 Astra

Status: verified against current OpenAI docs on 2026-09-09.

## Official sources

- Model guidance: https://developers.openai.com/api/docs/guides/latest-model
- Model page: https://developers.openai.com/api/docs/models/gpt-6-astra

## Verified model behaviors

OpenAI currently highlights five prompting areas for GPT‑6 Astra:

1. **Initiative and follow-through**: Astra may ask focused questions when missing information could change the result; for authorized reversible work, prompting should bias toward action rather than unnecessary approval pauses.
2. **Instruction following**: Astra follows instructions strongly and can be especially sensitive to Skills, `AGENTS.md`, and other instruction files. Audit silent or conflicting guidance.
3. **Personality and writing style**: Astra tends toward detailed, formatted responses and recurring phrasing. Specify the application’s desired style and structure when this matters.
4. **Subagent delegation**: Astra may delegate less than some harnesses want. Only tune delegation when the host actually provides subagents and parallelism is useful.
5. **Testing and verification**: Astra can over-verify coding work. Calibrate testing to the change and stop broadening once required checks pass unless new failures or risks justify more.

## Prompt adaptations

Use the Core first. Add Astra-specific rules only when the observed task needs them:

- For unnecessary confirmation: make authorized reversible scope, true blockers, and completion conditions explicit.
- For Skill/AGENTS conflicts: state instruction priority accurately and identify the exact file/rule that caused a pause or divergence.
- For over-formatting: request clear paragraphs and use lists/tables only where parallel, sequential, or comparative structure helps.
- For under-delegation: define when parallel subagents should be used; do not force delegation for tiny or sequential tasks.
- For over-testing: require project checks and affected-behavior verification; repeat or broaden only on new changes, failures, or unresolved concerns.

## API / runtime facts

- Model ID: `gpt-6-astra`.
- Current reasoning efforts: `low`, `medium`, `high`, `xhigh`, `max`. `none` is not supported.
- Context window: 1,050,000 tokens. Max output: 128,000 tokens.
- Tool calling with GPT‑6 Astra requires the Responses API; Chat Completions is otherwise supported.
- When migrating from `none` or `minimal`, OpenAI recommends starting with `low` and comparing results. Otherwise preserve the current effective effort unless evals justify a change.
- Remove unsupported sampling/logprob parameters listed in the current model guidance rather than encoding them as prompt text.
- Structured Outputs, prompt caching, compaction, persisted reasoning, computer use, and other host/API features must be configured through the API/harness, not simulated by prompt wording.

## Migration notes

Treat GPT‑6 Astra as a model to tune for rather than carrying all earlier-model workarounds forward. Audit especially:

- repeated approval rules,
- long prescriptive Skill/AGENTS instructions,
- forced repeated testing,
- fixed formatting workarounds,
- prompt text pretending to configure unsupported API parameters.

## Do not generalize

Do not copy these Astra-specific behaviors into other model profiles without evidence:

- the tendency toward detailed Markdown formatting,
- the tendency to over-verify coding work,
- the possibility of under-delegating relative to a multi-agent harness,
- GPT‑6 reasoning effort values,
- Responses-only tool calling,
- OpenAI-specific migration and caching fields.
