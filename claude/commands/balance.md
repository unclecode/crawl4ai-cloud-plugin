---
description: Show your Crawl4AI Cloud credit balance
allowed-tools:
  - mcp__plugin_crawl4ai_crawl4ai__balance
---

Call the Crawl4AI Cloud `balance` tool and show the answer in two or three short lines: the plan (its name and the day it renews, or Free), the free and plan credit, the bought credit and what this month cost.

If the balance is low, say what the user can do on the dashboard's Billing tab (https://crawl4ai.com/dashboard/#billing): start a plan, or on a plan buy extra credits. Do not call `topup`, `spend_cap` or `recharge`.
