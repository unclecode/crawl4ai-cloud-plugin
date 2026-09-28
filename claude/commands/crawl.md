---
description: Scrape many URLs, or a file of URLs, with Crawl4AI Cloud
argument-hint: <url> [url ...] | <file of urls>
allowed-tools:
  - mcp__plugin_crawl4ai_crawl4ai__estimate
  - mcp__plugin_crawl4ai_crawl4ai__batch
  - mcp__plugin_crawl4ai_crawl4ai__jobs_submit
  - mcp__plugin_crawl4ai_crawl4ai__jobs_status
  - mcp__plugin_crawl4ai_crawl4ai__jobs_results
  - Read
  - Write
---

Scrape these URLs with Crawl4AI Cloud: 

- If the input is a path to a file, read the file. It has one URL on each line.
- If no URL was given, ask the user for the URLs and stop.
- Follow the `bulk-crawl` skill: estimate first when there are more than 10 URLs and wait for the user's yes, use `batch` for up to 50 URLs and a job for 50 to 500.
- Save the pages under `.crawl4ai/` when there are more than 5, with the naming rule of the `scrape-to-files` skill.
- End with how many URLs worked and how many failed.
