---
description: Send a bug report, a feature request or feedback to the Crawl4AI team
argument-hint: <what you want to tell the team>
allowed-tools:
  - mcp__plugin_crawl4ai_crawl4ai__report_issue
---

The user wants to send this to the Crawl4AI team: 

1. If the text is empty, ask the user what they want to send and stop.
2. Pick the kind: `[bug]` for something that does not work, `[feature]` for a request, `[feedback]` for anything else.
3. Write the report:
   - `title`: the kind first, then one short line. Example: `[bug] extract returns empty data for a public page`.
   - `what_happened`: the user's text, and the URL, the tool and the `request_id` when they are known.
   - Remove the API key, other secrets and personal data from the text.
4. Show the user the exact `title` and `what_happened` and ask: "Send this to the Crawl4AI team?"
5. Call `report_issue` only after the user clearly says yes. If the user changes the text, show it again and ask again.
6. After the call, tell the user the report was sent. Do not share the report link; it is private to the team.
