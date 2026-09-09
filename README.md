# GPT‑6 提示词写作 Skill

把模糊需求写成 GPT‑6 Astra 可以执行、检查和交付的提示词。

A Chinese-first Codex skill for writing, refining, compressing, and diagnosing GPT‑6 Astra prompts, grounded in official OpenAI guidance.

适合从零写提示词、审计和精简旧提示词、把模糊质量要求转成可验收标准、修复 Agent 反复确认或过度测试，以及设计 API 结构化输出。默认先给一个可复制版本，再按需要附变量和使用说明。

## 先试一句

安装后，在 Codex 中输入：

```text
$gpt6-prompt-writer 帮我写一个 GPT6 提示词：面向 AI 新手，解释“先写清楚交付物，再补背景”，用于 150–200 字的小红书短文。只给最终提示词。
```

Skill 会生成供目标模型使用的提示词。需要它执行提示词里的业务任务时，再明确提出执行要求。

## 安装

需要支持 Skills 的 Codex 环境。安装需联网；提示词写作本身不需要 API key 或第三方 Python 包。

可直接告诉 Codex：

```text
$skill-installer 从 https://github.com/gnipbao/gpt6-prompt-writer 安装 gpt6-prompt-writer。分支为 codex/main，SKILL.md 位于仓库根目录。
```

也可以用 Codex 自带的安装脚本：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo gnipbao/gpt6-prompt-writer \
  --ref codex/main \
  --path . \
  --name gpt6-prompt-writer
```

默认安装到 `~/.codex/skills/gpt6-prompt-writer`，设置了 `CODEX_HOME` 时使用其 `skills` 子目录。已有同名目录时安装器会停止，避免覆盖。成功后在下一轮对话调用。

安装器用法依据 Codex 随附的 `skill-installer`；不同宿主的技能发现方式可能不同。

## 常见用法

| 目标 | 调用示例 |
| --- | --- |
| 从零生成 | `$gpt6-prompt-writer 给我一个每周整理工作记录的 GPT6 周报模板，其他你决定。` |
| 优化 Agent | `$gpt6-prompt-writer 优化这段 GPT6 编码提示词，让它在已授权范围内完成修复，减少无谓确认。下面是原文：……` |
| 压缩 | `$gpt6-prompt-writer 压缩这段提示词，保留所有事实、权限、输出格式和失败处理约束：……` |
| 只诊断 | `$gpt6-prompt-writer 只诊断以下 GPT6 提示词的冲突，不重写：……` |
| API 提取 | `$gpt6-prompt-writer 为 GPT6 设计课程报名信息提取提示词和 Responses 请求，姓名和课程可能缺失，下游需要稳定解析。` |

更多输入与成品见 [完整示例](examples/worked-examples.md)。

## GPT‑6 适配重点

依据 [官方 GPT‑6 Astra 指南](https://developers.openai.com/api/docs/guides/latest-model)，按任务需要加入这些控制：

- **可验收结果**：把“专业、深入、高质量”等抽象要求转成可观察的产物特征和完成标准。
- **Prompt 审计**：删除语义重复、无目的流程、旧模型 workaround 与无可观察效果的强化词；多个症状能由同一原则控制时合并为根因级指令。
- **目的上下文**：只有任务用途会改变重点、取舍、风险判断或输出结构时才写入，不为背景完整堆无关信息。
- **自主完成**：先区分分析、建议和执行；明确行动意图在已授权范围内推进，不把问题描述扩成未授权修改。
- **状态真实性**：计划、推断和意图不升级成“已搜索/已验证/已完成”；状态有实际支持，证据默认按需披露。
- **指令冲突**：区分用户目标、技能建议和平台系统/开发者约束。
- **写作风格**：写清读者、篇幅与表达形式，把“专业/去 AI 味”等模糊风格词转成具体写作行为；简洁靠信息选择，不靠电报体。
- **协作分工**：仅在宿主提供并允许子代理时，描述独立分工和整合责任。
- **适量验证**：完成项目必需检查和相关行为验证，以新问题决定是否扩大测试。
- **行为保真压缩**：优先减少 instruction surface area，保留目标、权限、事实边界、格式和失败处理等不变量。

API 配置与自然语言提示词分开处理；模型与参数事实见 [API 契约](references/api-contract.md)。模板和选择规则属于本项目的实现，不代表 OpenAI 的统一规定。

部分通用提示词工程原则也参考其他前沿模型的官方指南，用于补充 Prompt Audit、任务用途、状态真实性、可读性和示例策略；这些内容记录在 [跨模型提示词工程参考](references/cross-model-notes.md)，明确标为本项目工程选择，不作为 GPT‑6 官方规则，也不迁移其他模型的格式偏好、effort 默认值或专属运行时行为。

## 文件结构

```text
gpt6-prompt-writer/
├── SKILL.md                       # 触发条件、工作流程与输出约定
├── agents/openai.yaml             # Codex 显示名称与默认提示
├── references/
│   ├── gpt6-best-practices.md     # 官方依据及规则映射
│   ├── prompt-patterns.md         # 按需选用的提示词模块
│   ├── cross-model-notes.md       # 跨模型通用工程原则与不迁移项
│   └── api-contract.md            # API 角色、参数和 schema 边界
├── examples/
│   ├── worked-examples.md         # 完整写作示例
│   ├── extraction-request.json    # 合法 JSON 请求体示例
│   ├── retest-prompts.json        # 18 个 GPT-6 核心待执行回归场景
│   └── retest-cross-model-prompts.json # 6 个跨模型工程原则待执行回归场景
├── scripts/validate.py            # 无第三方依赖的静态校验
└── LICENSE
```

## 校验与证据范围

在仓库根目录运行（Python 3.10+）：

```bash
python3 scripts/validate.py
```

脚本检查 Skill 元数据、显式调用策略、必需文件、相对引用、JSON 语法、两组回归用例格式，以及示例请求的模型/字段/schema 约束。GitHub Actions 执行同一命令。它不联网、不调用模型，也不是完整 JSON Schema 验证器或安全扫描器。

当前为初版试用：结构检查通过；六个场景做过同一上下文的人工推演（E2 / dry-run）；尚无独立模型回放、真实 API 兼容性实测或成功率数据。当前共有 **24 个待执行回归场景（18 个 GPT‑6 核心 + 6 个跨模型工程原则）**，不能当作 24 次测试通过记录。

修改提示词行为后，选择相关正常、缺信息、冲突输入做真实回放，记录版本、实际输出与失败条件。请勿将私密原始对话或凭据提交为测试材料。

## 依据与维护

OpenAI 官方资料核验日期为 **2026-09-07**，目标为 **GPT‑6 Astra / `gpt-6-astra`**。动态指南将来可能指向新模型；用户明确指定 GPT‑6 时应继续核对它的专属资料，不自动换代。

GPT‑6 出处与证据边界见 [来源记录](references/gpt6-best-practices.md)。跨模型工程参考于 **2026-09-09** 核验 Anthropic 的 [Fable 5.1 提示词指南](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) 与 [Fable 5 提示词指南](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)，只吸收可泛化的工程原则；模型特有行为不自动迁移。离线时可使用注明日期的快照；要求“最新”或可运行 API 配置时应重新查阅官方资料。

本项目为社区 Skill。执行外部操作、工具权限和模型调用均由使用它的宿主负责；文本提示词不会自行开启工具或获得新权限。

## 许可证

本仓库的原创指令、示例与脚本按 [MIT License](LICENSE) 开源。链接指向的外部文档保留其各自的权利和条款。
