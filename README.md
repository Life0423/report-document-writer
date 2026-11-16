# Report & Document Writer

An evidence-first AI skill for Chinese reports and formal documents.

用于中文报告与正式文书的撰写、改写、审校、风格匹配和交付检查。以真实材料为依据，不编造数据、文献、经历或完成状态。

## What it does / 能力

- 课程与实验报告、项目报告、调研报告、总结与方案。
- 申请书、说明、通知、会议纪要等正式文书。
- 明确受众、模板和事实边界，组织证据与结构，再完成成稿。
- 复核数字、引用、术语、排版与待补充项。

## Use / 使用

Install the `skills/report-document-writer` directory in an assistant that supports agent skills, following that host's installation instructions. The skill is text-based and requires no API keys or custom service. Document rendering, web research and file export depend on the host's available tools.

支持隐式调用的宿主可依据任务描述自动选用本技能；也可明确要求使用 `report-document-writer`。实际触发行为由宿主控制，本仓库不会自动修改任何账号设置。

Example prompt:

> 使用 report-document-writer，根据我提供的材料和模板撰写项目报告。先区分已验证结果与待完成工作，保持事实和数据可追溯，缺失信息标为待补充。

## Layout

- `skills/report-document-writer/SKILL.md`: workflow and activation description
- `skills/report-document-writer/references/`: document patterns and delivery checklist
- `skills/report-document-writer/agents/openai.yaml`: optional host metadata
- `skills/report-document-writer/assets/icon.svg`: project icon

## Privacy and iteration / 隐私与迭代

Improve reusable methods from feedback, not by collecting private task content. Public changes should contain generalized rules and synthetic or properly anonymized examples only. Do not commit private reports, raw conversations, personal writing samples, credentials, account identifiers or confidential source material. Review diffs and run representative checks before publishing an update.

This skill drafts documents; it does not itself authorize sending, submitting, publishing or signing them. It is not a substitute for qualified legal, medical or financial review.

## License and attribution

MIT. Maintained by Life0423. Developed with AI assistance. The public package contains the project skill and its supporting files, not third-party tool implementations or private task data.
