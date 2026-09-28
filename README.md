# Crawl4AI Cloud plugin

This repository holds plugins that connect coding agents to [Crawl4AI Cloud](https://crawl4ai.com).
Crawl4AI Cloud is the hosted API of the open-source crawler [Crawl4AI](https://github.com/unclecode/crawl4ai).
It turns web pages into clean markdown, searches the web, extracts typed JSON and crawls many URLs.

Today the repository has a plugin for Claude Code. Plugins for other agents come later (see [Other agents](#other-agents)).

The plugin uses the Crawl4AI Cloud remote MCP server at `https://api.crawl4ai.com/mcp`.
You install nothing else: no command-line tool and no local server.

## Get an API key

1. Open https://crawl4ai.com and click "Get a key".
2. Verify your email to get a permanent key and the signup credit.
3. Manage your keys and your credit on the dashboard: https://crawl4ai.com/dashboard/

Each call costs credits. The prices are on https://crawl4ai.com.

## Install in Claude Code

### In the chat

```
/plugin marketplace add unclecode/crawl4ai-cloud-plugin
/plugin install crawl4ai@crawl4ai-cloud
```

Claude Code asks for your API key when it enables the plugin. If it does not ask, or to change the key later, run:

```
/plugin configure crawl4ai@crawl4ai-cloud
```

### In the terminal

```
claude plugin marketplace add unclecode/crawl4ai-cloud-plugin
claude plugin install crawl4ai@crawl4ai-cloud
```

Then start Claude Code and run `/plugin configure crawl4ai@crawl4ai-cloud` to give your key.

You can also give the key in the install command. Warning: the key then stays in your shell history.

```
claude plugin install crawl4ai@crawl4ai-cloud --config api_key=<your key>
```

### Where the key goes

Claude Code keeps the key in its secure credential store, not in `settings.json` and not in your project.
The plugin sends it only to the Crawl4AI server, in the `Authorization` header.

### Your own server

If you run your own Crawl4AI Cloud server, set the `base_url` option (for example `https://crawl.example.org`).
The default is `https://api.crawl4ai.com`.

## What you get

### Skills

Claude uses a skill by itself when your task fits it. You can also call one by name, for example `/crawl4ai:web-research`.

| Skill | What it does |
|---|---|
| `web-research` | Answers a question from the web. It searches, reads the best 3 to 5 pages and gives the source URLs. |
| `scrape-to-files` | Saves 1 to 10 pages as markdown files under `.crawl4ai/` in your project. It runs in its own context, so the page text stays out of the chat. |
| `extract-data` | Gets typed JSON from a page, from an instruction or a JSON schema. |
| `bulk-crawl` | Scrapes more than 10 URLs and can save them as files. It shows the cost estimate first and waits for your yes. Up to 50 URLs run in one batch, 50 to 500 as a background job. |
| `recipes` | Runs a ready-made scraper for a known site. Not open yet: the skill checks and tells you. |
| `watch` | Watches a page and reports the changes you care about. In private preview: the skill checks and tells you. |

### Commands

| Command | What it does |
|---|---|
| `/crawl4ai:scrape <url>` | Scrapes one page to markdown. |
| `/crawl4ai:search <query>` | Searches the web and lists the results. |
| `/crawl4ai:extract <url> <what>` | Extracts the data you describe as JSON. |
| `/crawl4ai:crawl <urls or a file of urls>` | Scrapes many URLs. |
| `/crawl4ai:balance` | Shows your credit. |
| `/crawl4ai:feedback <text>` | Sends a bug report, a feature request or feedback to the Crawl4AI team. It shows you the exact text and waits for your yes. |

### Agent

`web-researcher` does long research in its own context and returns a short summary with sources.

### MCP tools

The plugin adds the MCP server `crawl4ai`. Its tools have names like `mcp__plugin_crawl4ai_crawl4ai__scrape`.

| Tool | What it does |
|---|---|
| `scrape` | One page to markdown or HTML. |
| `search` | Web search with ranked results. |
| `answer` | A direct answer with sources. Experimental. |
| `extract` | Typed data from a page. |
| `batch` | Up to 50 URLs in one call. |
| `jobs_submit`, `jobs_status`, `jobs_results` | 50 to 500 URLs as a background job. |
| `estimate` | The credit range of a call before it runs. |
| `balance` | Your credit. |
| `recipes_list`, `recipe_run` | Ready-made scrapers (not open yet). |
| `watch_page`, `list_changes` | Page change monitors (private preview). |
| `topup`, `spend_cap`, `recharge` | Credit and billing settings. The skills never call these without your clear yes. |
| `report_issue` | Sends a report to the Crawl4AI team. |

## Tips

- Add `.crawl4ai/` to your `.gitignore` if you do not want saved pages in your repository.
- A page that needs a real browser can take up to 90 seconds. Let the call run.
- Out of credit (HTTP 402): top up on the dashboard at https://crawl4ai.com/dashboard/.
- In headless mode (`claude -p`), allow the tools, for example
  `claude -p --allowedTools "mcp__plugin_crawl4ai_crawl4ai" "Skill" "<your prompt>"`.

## Other agents

Plugins for these agents are coming soon. Today you can connect each one to the same MCP server with one line:

| Agent | Folder |
|---|---|
| Codex | [codex/](codex/README.md) |
| Cursor | [cursor/](cursor/README.md) |
| Gemini CLI | [gemini/](gemini/README.md) |
| OpenCode | [opencode/](opencode/README.md) |
| OpenClaw | [openclaw/](openclaw/README.md) |
| Pi | [pi/](pi/README.md) |
| Hermes | [hermes/](hermes/README.md) |
| Grok | [grok/](grok/README.md) |

The full API, written for agents: https://crawl4ai.com/llms.txt

## Links

- Crawl4AI Cloud: https://crawl4ai.com
- API docs: https://crawl4ai.com/docs/
- Dashboard: https://crawl4ai.com/dashboard/
- Open-source Crawl4AI: https://github.com/unclecode/crawl4ai

## License

Apache-2.0. See [LICENSE](LICENSE).
