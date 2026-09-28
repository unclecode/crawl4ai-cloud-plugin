# Crawl4AI Cloud for OpenCode

A plugin for OpenCode is coming soon.

## Use it today

Get an API key at https://crawl4ai.com (the dashboard: https://crawl4ai.com/dashboard/).

Then send this one line to OpenCode. Put your own key after `key:`.

```
set up crawl4ai - https://crawl4ai.com/llms.txt with key: <your key>
```

The agent reads the setup steps from that file and adds the Crawl4AI MCP server to its own config.

To do it by hand, add this to `opencode.json`:

```json
"mcp": { "crawl4ai": { "type": "remote", "url": "https://api.crawl4ai.com/mcp", "headers": { "Authorization": "Bearer <your key>" } } }
```

Restart OpenCode if the tools do not show.
