#!/usr/bin/env python3
"""Static checks for the multi-model prompt-writer package; no network/model execution."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL_PROFILES = (
    "references/models/openai/gpt-6-astra.md",
    "references/models/openai/gpt-5.6.md",
    "references/models/anthropic/claude-fable-5.md",
    "references/models/anthropic/claude-fable-5.1.md",
    "references/models/google/gemini-3.x.md",
    "references/models/xai/grok-4.6.md",
    "references/models/deepseek/deepseek-v4.md",
    "references/models/zhipu/glm-5.x.md",
    "references/models/volcengine/doubao-seed-2.x.md",
)
MODEL_EVALS = (
    "evals/models/openai/gpt-6-astra.json",
    "evals/models/openai/gpt-5.6.json",
    "evals/models/anthropic/claude-fable-5.json",
    "evals/models/anthropic/claude-fable-5.1.json",
    "evals/models/google/gemini-3.x.json",
    "evals/models/xai/grok-4.6.json",
    "evals/models/deepseek/deepseek-v4.json",
    "evals/models/zhipu/glm-5.x.json",
    "evals/models/volcengine/doubao-seed-2.x.json",
)
REQUIRED_FILES = (
    "SKILL.md", "README.md", "agents/openai.yaml",
    "references/core/prompt-principles.md", "references/core/prompt-patterns.md",
    "evals/core.json", "examples/worked-examples.md", "examples/extraction-request.json",
    *MODEL_PROFILES, *MODEL_EVALS,
)
LEGACY_FLAT_PATHS = (
    "references/models/gpt-6-astra.md",
    "references/models/claude-fable-5.md",
    "references/models/claude-fable-5.1.md",
    "references/models/grok-4.6.md",
    "evals/models/gpt-6-astra.json",
    "evals/models/claude-fable-5.json",
    "evals/models/claude-fable-5.1.json",
    "evals/models/grok-4.6.json",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_eval(path: Path, seen_ids: set[str]) -> int:
    data = read_json(path)
    require(data.get("schema_version") == 2, f"Unexpected eval schema: {path}")
    cases = data.get("cases")
    require(isinstance(cases, list) and cases, f"No eval cases: {path}")
    for case in cases:
        cid = case.get("id")
        require(isinstance(cid, str) and cid, f"Missing case id: {path}")
        require(cid not in seen_ids, f"Duplicate case id: {cid}")
        seen_ids.add(cid)
        require(isinstance(case.get("prompt"), str) and case["prompt"].strip(), f"Missing prompt: {cid}")
        for key in ("must", "must_not"):
            values = case.get(key)
            require(isinstance(values, list) and values, f"Missing {key}: {cid}")
            require(all(isinstance(x, str) and x.strip() for x in values), f"Bad {key}: {cid}")
    return len(cases)


def check_strict_objects(node) -> None:
    if isinstance(node, dict):
        if node.get("type") == "object":
            props = node.get("properties", {})
            req = node.get("required", [])
            require(node.get("additionalProperties") is False, "Schema object must set additionalProperties=false")
            require(set(req) == set(props) and len(req) == len(props), "Every object property must be required once")
        for value in node.values():
            check_strict_objects(value)
    elif isinstance(node, list):
        for value in node:
            check_strict_objects(value)


def validate() -> int:
    for rel in REQUIRED_FILES:
        require((ROOT / rel).is_file(), f"Missing file: {rel}")
    for rel in LEGACY_FLAT_PATHS:
        require(not (ROOT / rel).exists(), f"Legacy flat model path still present: {rel}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", skill, re.S)
    require(match is not None, "SKILL.md needs YAML frontmatter")
    frontmatter, body = match.groups()
    fields: dict[str, str] = {}
    for line in frontmatter.splitlines():
        key, sep, value = line.partition(":")
        require(bool(sep) and key not in fields, "Malformed or duplicate frontmatter field")
        fields[key] = value.strip()
    require(set(fields) == {"name", "description", "disable-model-invocation"}, "Unexpected frontmatter fields")
    require(fields["name"] == "multi-model-prompt-writer", "Unexpected skill name")
    require(fields["disable-model-invocation"] == "true", "Claude-style explicit invocation must remain enabled")
    require(100 <= len(fields["description"]) <= 1024, "Description length outside expected range")
    require(len(body.splitlines()) <= 500, "Move details out of SKILL.md")
    for heading in ("## 核心原则", "## 工作流程", "## 边界", "## 质量标准"):
        require(heading in body, f"Missing section: {heading}")

    openai_meta = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    require("allow_implicit_invocation: false" in openai_meta, "OpenAI-style explicit invocation must remain enabled")
    require("$multi-model-prompt-writer" in openai_meta, "OpenAI default prompt uses old skill name")

    for rel in MODEL_PROFILES:
        require(f"`{rel}`" in body, f"Reference missing from SKILL resource guide: {rel}")
        text = (ROOT / rel).read_text(encoding="utf-8")
        require("## Official sources" in text, f"Model profile lacks official sources: {rel}")
        require("## Do not generalize" in text, f"Model profile lacks Do not generalize: {rel}")
        require("Status:" in text, f"Model profile lacks verification status: {rel}")

    markdown = [ROOT / "README.md", ROOT / "SKILL.md", ROOT / "examples/worked-examples.md"]
    markdown += sorted((ROOT / "references").rglob("*.md"))
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        require(text.count("```") % 2 == 0, f"Unbalanced fences: {path}")
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if link.startswith(("https://", "http://", "#")):
                continue
            dest = (path.parent / link.split("#")[0]).resolve()
            require(dest.is_relative_to(ROOT) and dest.exists(), f"Broken/outside relative link in {path}: {link}")

    seen_ids: set[str] = set()
    count = check_eval(ROOT / "evals/core.json", seen_ids)
    for rel in MODEL_EVALS:
        count += check_eval(ROOT / rel, seen_ids)

    request = read_json(ROOT / "examples/extraction-request.json")
    require(request.get("model") == "gpt-6-astra", "GPT-6 extraction example model drift")
    require(request.get("reasoning", {}).get("effort") == "low", "GPT-6 extraction example baseline drift")
    fmt = request["text"]["format"]
    require(fmt.get("type") == "json_schema" and fmt.get("strict") is True, "GPT-6 extraction example must use strict Structured Outputs")
    check_strict_objects(fmt["schema"])

    primary = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in ("SKILL.md", "README.md", "agents/openai.yaml"))
    require("gpt6-prompt-writer" not in primary, "Old repository/skill name remains in primary docs")
    require("--repo chrisjian/multi-model-prompt-writer" in primary, "README installer repo drift")

    print(f"PASS: multi-model architecture, explicit invocation, {len(MODEL_PROFILES)} model/family profiles, {count} eval cases, vendor paths, and GPT-6 API example contracts.")
    print("Static checks only; no model/API execution or performance claim.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(validate())
    except (ValueError, KeyError, TypeError, OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
