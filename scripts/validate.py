#!/usr/bin/env python3
"""Static checks for this skill package; no network or model execution."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "SKILL.md", "README.md", "LICENSE", "agents/openai.yaml",
    "references/gpt6-best-practices.md", "references/prompt-patterns.md",
    "references/cross-model-notes.md", "references/api-contract.md",
    "examples/worked-examples.md", "examples/extraction-request.json",
    "examples/retest-prompts.json", "examples/retest-cross-model-prompts.json",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_objects(node) -> None:
    """Check only strict-object invariants used by the bundled schema."""
    if isinstance(node, dict):
        if node.get("type") == "object":
            properties = node.get("properties", {})
            required = node.get("required", [])
            require(node.get("additionalProperties") is False,
                    "Schema objects must set additionalProperties=false")
            require(set(required) == set(properties) and len(required) == len(properties),
                    "Every schema object property must appear once in required")
        for value in node.values():
            check_objects(value)
    elif isinstance(node, list):
        for value in node:
            check_objects(value)


def check_fixture(path: Path, seen_ids: set[str]) -> int:
    fixtures = read_json(path)
    require(fixtures["target_model"] == "gpt-6-astra", f"Unexpected fixture target model: {path.name}")
    cases = fixtures["cases"]
    require(bool(cases), f"No regression inputs: {path.name}")
    ids = [case["id"] for case in cases]
    require(len(ids) == len(set(ids)), f"Duplicate regression case IDs within {path.name}")
    require(not seen_ids.intersection(ids), f"Duplicate regression case IDs across fixture files: {path.name}")
    seen_ids.update(ids)
    for case in cases:
        require(isinstance(case["prompt"], str) and bool(case["prompt"].strip()),
                f"Missing prompt: {case['id']}")
        for key in ("must", "must_not"):
            require(isinstance(case[key], list) and bool(case[key])
                    and all(isinstance(item, str) and bool(item.strip()) for item in case[key]),
                    f"Missing criteria {key}: {case['id']}")
    return len(cases)


def validate() -> int:
    for name in REQUIRED_FILES:
        require((ROOT / name).is_file(), f"Missing file: {name}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", skill, re.S)
    require(match is not None, "SKILL.md needs YAML frontmatter")
    frontmatter, body = match.groups()
    fields = {}
    for line in frontmatter.splitlines():
        key, sep, value = line.partition(":")
        require(bool(sep) and key not in fields, "Malformed or duplicate frontmatter field")
        fields[key] = value.strip()
    require(set(fields) == {"name", "description", "disable-model-invocation"},
            "Unexpected frontmatter fields")
    require(fields["name"] == "gpt6-prompt-writer", "Unexpected skill name")
    require(fields["disable-model-invocation"] == "true",
            "Claude Code skill must require explicit invocation")
    require(80 <= len(fields["description"]) <= 1024, "Description length outside expected range")
    require(len(body.splitlines()) <= 500, "Move details out of SKILL.md")
    for heading in ("## 工作流程", "## 边界", "## 质量标准"):
        require(heading in body, f"Missing section: {heading}")

    openai_meta = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    require("policy:\n  allow_implicit_invocation: false\n" in openai_meta,
            "Codex skill must require explicit invocation")

    markdown = [ROOT / "README.md", ROOT / "SKILL.md"]
    markdown += sorted((ROOT / "references").glob("*.md"))
    markdown += sorted((ROOT / "examples").glob("*.md"))
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        require(text.count("```") % 2 == 0, f"Unbalanced fences: {path.name}")
        for block in re.findall(r"```json\n(.*?)\n```", text, re.S):
            json.loads(block)
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if link.startswith(("https://", "http://", "#")):
                continue
            destination = (path.parent / link.split("#")[0]).resolve()
            require(destination.is_relative_to(ROOT) and destination.exists(),
                    f"Broken/outside relative link in {path.name}: {link}")
    for ref in (ROOT / "references").glob("*.md"):
        name = ref.relative_to(ROOT).as_posix()
        require(f"`{name}`" in body, f"Reference missing from resource guide: {name}")

    seen_ids: set[str] = set()
    case_count = 0
    for fixture_name in ("retest-prompts.json", "retest-cross-model-prompts.json"):
        case_count += check_fixture(ROOT / "examples" / fixture_name, seen_ids)

    request = read_json(ROOT / "examples/extraction-request.json")
    require(request["model"] == "gpt-6-astra", "Unexpected example model")
    require(request["reasoning"]["effort"] == "low", "Example migration baseline must be low")
    unsupported = {"temperature", "top_p", "top_logprobs", "logprobs", "response_format"}
    require(not unsupported.intersection(request), "Unsupported/mismatched example parameters")
    require(bool(request["instructions"]) and bool(request["input"]), "Missing example prompt")
    fmt = request["text"]["format"]
    require(fmt["type"] == "json_schema" and fmt["strict"] is True,
            "Example requires strict Structured Outputs")
    require(bool(fmt["name"]), "Missing schema name")
    schema = fmt["schema"]
    require(schema["type"] == "object" and "anyOf" not in schema, "Schema root must be object")
    check_objects(schema)

    examples = (ROOT / "examples/worked-examples.md").read_text(encoding="utf-8")
    samples = [json.loads(block) for block in re.findall(r"```json\n(.*?)\n```", examples, re.S)]
    require(bool(samples), "Missing designed extraction results")
    for sample in samples:
        require(set(sample) == set(schema["properties"]), "Example fields do not match schema")
        require(all(sample[key] is None or isinstance(sample[key], str) for key in ("name", "course")),
                "Example field types do not match")
        missing = [key for key in ("name", "course") if sample[key] is None]
        require(sample["missing_fields"] == missing, "Incorrect example missing_fields")
        require(sample["status"] == ("missing" if missing else "ok"), "Incorrect example status")

    print(f"PASS: metadata, explicit-invocation policy, files, links, JSON, {case_count} regression inputs, and example request contracts.")
    print("Static checks only; no model/API execution or performance claim.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(validate())
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
