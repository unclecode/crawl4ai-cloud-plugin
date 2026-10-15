# Crawl4AI Cloud plugin

This repository holds plugins that connect coding agents to [Crawl4AI Cloud](https://crawl4ai.com).
Crawl4AI Cloud is the hosted API of the open-source crawler [Crawl4AI](https://github.com/unclecode/crawl4ai).
It turns web pages into clean markdown, searches the web, gives Google's results page as data with true ranks (SERP),
extracts typed JSON and crawls many URLs.

Today the repository has a plugin for Claude Code. Plugins for other agents come later (see [Other agents](#other-agents)).

The plugin uses the Crawl4AI Cloud remote MCP server at `https://api.crawl4ai.com/mcp`.
You install nothing else: no command-line tool and no local server.

## Get an API key

1. Open https://crawl4ai.com and click "Get a key".
2. Verify your email to get a permanent key and 1,000 free credits every month.
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
| `scrape-to-files` | Saves pages as markdown files under `.crawl4ai/` in your project. It runs in its own context, so the page text stays out of the chat. It writes only inside `.crawl4ai/`. |
| `google-serp` | Gets Google's results page as data: the rank of each result and the blocks Google showed, for a country or a city. For rank tracking and SEO. |
| `extract-data` | Gets typed JSON from a page, from an instruction or a JSON schema. |
| `bulk-crawl` | Saves more than 10 URLs as files. It shows the cost estimate first and waits for your yes. Then `scrape-to-files` saves the pages: up to 50 in one batch, 51 to 500 as a background job. |
| `recipes` | Runs a ready-made scraper for a known site. Not open yet: the skill checks and tells you. |
| `watch` | Watches a page and reports the changes you care about, reads them, and stops or pauses a watch. In private preview. |

### Commands

| Command | What it does |
|---|---|
| `/crawl4ai:scrape <url>` | Scrapes one page to markdown. |
| `/crawl4ai:search <query>` | Searches the web and lists the results. |
| `/crawl4ai:serp <query> [in <place>]` | Shows Google's results page for a query: ranks, domains and the blocks Google showed. |
| `/crawl4ai:extract <url> <what>` | Extracts the data you describe as JSON. |
| `/crawl4ai:crawl <urls or a file of urls>` | Scrapes and saves many URLs under `.crawl4ai/`. |
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
| `serp` | Google's results page as data: true ranks and the blocks Google showed, for a country or a city. Beta. |
| `answer` | A direct answer with sources. Experimental. |
| `extract` | Typed data from a page. |
| `batch` | Up to 50 URLs in one call. |
| `jobs_submit`, `jobs_status`, `jobs_results` | 50 to 500 URLs as a background job. |
| `estimate` | The credit range of a call before it runs. |
| `balance` | Your credit and your plan. |
| `plans` | The monthly plans (Starter, Builder, Scale) and where to start one. |
| `recipes_list`, `recipe_run` | Ready-made scrapers (not open yet). |
| `site_crawl`, `site_scan` | Crawl a whole site, or list every URL of a site (coming soon). |
| `watch_page`, `watch_changes`, `list_changes`, `stop_watching`, `resume_watching` | Page change monitors (private preview). |
| `topup`, `spend_cap`, `recharge` | Extra credits on a plan, your own monthly cap, auto-recharge. They spend or limit money: the skills never call them without your clear yes. |
| `report_issue` | Sends a report to the Crawl4AI team. |

## Watch changes in your session

Watch can push its changes into a running Claude Code session, so the agent learns about a change with no timer.
This uses Claude Code channels, which are a research preview. Start the session like this:

```
CRAWL4AI_WATCH_CHANNEL=1 claude --dangerously-load-development-channels plugin:crawl4ai@crawl4ai-cloud
```

Claude Code shows a warning about development channels: select "I am using this for local development".
A new change then appears in the session as a line that starts with `← watch:`.

- The channel reads your Watch feed and marks the changes read. It reads only in a session started with
  `CRAWL4AI_WATCH_CHANNEL=1`. In every other session it does nothing.
- To read only one agent's monitors, also set `CRAWL4AI_AGENT=<label>`.
- It needs `python3` (3.9 or newer). It runs only while the session is open.
- Until Crawl4AI is on Anthropic's channel allowlist, the development flag is needed.

## Tips

- Saving a long page runs a small script from the plugin with `python3` (3.9 or newer). macOS and most Linux systems have it.
- Add `.crawl4ai/` to your `.gitignore` if you do not want saved pages in your repository.
- A page that needs a real browser can take up to 90 seconds. Let the call run.
- Out of credit or over a limit (HTTP 402 or 429): the answer says why and gives the link. A free account starts a plan; a plan buys extra credits on the dashboard's Billing tab.
- In headless mode (`claude -p`), allow the tools you need. Put the prompt first, because `--allowedTools` takes every word after it. Do not allow the whole server: that also allows `topup`, `spend_cap` and `recharge`, which spend money.

  ```
  claude -p "<your prompt>" --allowedTools Skill \
    mcp__plugin_crawl4ai_crawl4ai__search mcp__plugin_crawl4ai_crawl4ai__answer \
    mcp__plugin_crawl4ai_crawl4ai__scrape mcp__plugin_crawl4ai_crawl4ai__batch \
    mcp__plugin_crawl4ai_crawl4ai__extract mcp__plugin_crawl4ai_crawl4ai__estimate
  ```

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
