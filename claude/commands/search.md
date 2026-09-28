---
description: Search the web with Crawl4AI Cloud
argument-hint: <query>
allowed-tools:
  - mcp__plugin_crawl4ai_crawl4ai__search
---

Search the web with the Crawl4AI Cloud `search` tool for: $ARGUMENTS

- If no query was given, ask the user for one and stop.
- Show the results as a numbered list: the title, the URL and a one-line snippet.
- Do not scrape the results. The user can run `/crawl4ai:scrape <url>` on the one they want.
- On a 402 `no_credit` answer, tell the user to top up on the dashboard at https://crawl4ai.com/dashboard/.
