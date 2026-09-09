# Repository Guidelines

## Model Profile admission

A Model Profile exists only when the target model has a reusable difference that materially changes how the natural-language prompt should be written.

Do not add Profile content merely to document model support.

Exclude from Model Profiles:

- product positioning, benchmarks, and capability summaries;
- API parameters, model IDs, context/output limits, protocol, or state mechanics;
- harness-specific tools, permissions, rules, or configuration;
- principles already covered by Core;
- statements that evidence is unavailable or that Core should be used;
- maintenance, verification, or source-audit notes.

Before adding a Profile rule, ask:

> For the same user goal, would this evidence cause us to write a materially different natural-language prompt for this model?

If not, do not add it. If no meaningful prompt delta remains, the model is Core-only and should not have a Profile file.

## Duplication

Do not repeat Core rules inside Model Profiles. Do not repeat API routing rules across Profiles or references. Prefer deleting redundant instructions over paraphrasing them.

## Layering

- Core: model-neutral prompt behavior.
- Model Profile: model-specific natural-language prompt deltas only.
- API reference: programmatic parameters, protocol, state, and integration details.
- Harness behavior: verify at task time when the task depends on it; do not encode it as model behavior.

## Evals

Do not add regression cases merely to prove a refactor or repository-structure change. Add an eval when it captures a real user requirement, observed failure, or meaningful model-specific behavior. Preserve existing cases unless they are genuinely obsolete; keep validation proportional to the change.
