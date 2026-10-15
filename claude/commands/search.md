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
- On a 402 or 429 answer (out of credit, a plan's monthly allowance, the user's own spend cap, the free speed limit): show the user the answer's own message and its link; a free account's answer carries the link to start a plan.
