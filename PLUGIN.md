# goodWriter plugin

This repository is a skills-only **Agent Plugins 1.0** package. The original `skills/good-writer` remains the single source of truth, so standalone skill users keep working. No MCP server, external service, credentials, lifecycle hooks, or paid dependency is required.

## ChatGPT web

Packaging is not installation. To use this on the web, create/import a cloud plugin and install it in the intended account/workspace. A local desktop marketplace alone does not register a web plugin.

- **Plugin Creator:** In a workspace where creation is available, open Plugin Creator and ask it to create a skills-only plugin from this package, preserving all skill files. Review and install its resulting plugin, then test in a new conversation with `@goodWriter`.
- **Workspace GitHub import (admin):** Open **Admin > Plugins > Add > Import marketplace**. Source: `https://github.com/Life0423/report-document-writer`; Path: empty; Branch: `main`. Review the import and access policy, then install the plugin. This supports later repository sync. Importing is separate from public directory submission.

The package does not grant permissions, force every custom GPT to load it, read all chats, or create a background scheduler. Host settings and available tools still apply. The skill's implicit trigger is retained, but explicitly selecting the plugin is the reliable way to test availability.

## Local clients

In supported Codex clients:

```sh
codex plugin marketplace add Life0423/report-document-writer --ref main
```

Open the supported client's plugin directory, select the goodWriter source, install `good-writer`, and start a new session. Desktop/local installation is not proof of web installation.

## Build and check

```sh
python scripts/package_plugin.py
```

This validates the local package, checks skill references and original eval data, and produces `dist/good-writer-1.0.0.zip` plus its SHA-256. It does not install or publish anything. The archive excludes Git metadata, private files, and build outputs.

Behavioral smoke tests after installation:

1. “使用 goodWriter，只根据‘10 个测试全部通过’写总结。” It must not invent struggles, feelings, or growth. Any material question belongs outside the draft.
2. “使用 goodWriter，只改第二段，其他内容不要动。” It must respect the revision scope.
3. “使用 goodWriter，写一份会议通知。” It must use the formal document purpose, not student reflection.
4. Review all 14 fictional cases in `skills/good-writer/evals/cases.json`.

Structural validation is not a substitute for an actual new-chat web test. The archive is not evidence that a cloud plugin has been installed.

## Maintenance and privacy

Keep generic improvements and synthetic tests in the existing skill directory; bump the plugin version for releases. Never publish raw conversations, private reports or screenshots. Scheduled review remains a separately authorized host automation, not code inside this plugin. Updating GitHub does not necessarily refresh an installed archive: reimport/update that plugin or use workspace GitHub sync. No universal directory submission has been performed by this package.

## Official references

- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Build plugins in ChatGPT](https://learn.chatgpt.com/docs/build-plugins)
- [Import and sync plugins from GitHub](https://learn.chatgpt.com/docs/enterprise/plugin-management)
