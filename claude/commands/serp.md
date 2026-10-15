---
description: Google's results page as data, with true ranks, with Crawl4AI Cloud
argument-hint: <query> [in <city or country>]
allowed-tools:
  - mcp__plugin_crawl4ai_crawl4ai__serp
---

Get Google's results page with the Crawl4AI Cloud `serp` tool for: $ARGUMENTS

- If no query was given, ask the user for one and stop.
- If the text names a place ("in Berlin", "in Germany"), pass it as `location` or `country`, not inside `q`.
- Show the organic results as a table: rank, title, and the site from the url. Then name the blocks Google showed, in page order.
- On a 400 for an unknown location, show the 3 closest names it gives and ask the user to pick one.
- On a 402 `no_credit` answer, tell the user to add credit on the dashboard at https://crawl4ai.com/dashboard/.
