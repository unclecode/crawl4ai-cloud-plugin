---
description: Scrape and save many URLs, or a file of URLs, with Crawl4AI Cloud
argument-hint: <url> [url ...] | <file of urls>
allowed-tools:
  - mcp__plugin_crawl4ai_crawl4ai__estimate
  - Read
  - Skill(crawl4ai:bulk-crawl)
  - Skill(crawl4ai:scrape-to-files)
---

Scrape and save these URLs with Crawl4AI Cloud: $ARGUMENTS

- If the input is a path to a file, read the file. It has one URL on each line.
- If no URL was given, ask the user for the URLs and stop.
- 1 to 10 URLs: call the `crawl4ai:scrape-to-files` skill with the URLs.
- More than 10 URLs: follow the `crawl4ai:bulk-crawl` skill. It shows the estimate and waits for the user's yes.
- End with how many URLs were saved and how many failed.
