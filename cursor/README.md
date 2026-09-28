# Crawl4AI Cloud for Cursor

A plugin for Cursor is coming soon.

## Use it today

Get an API key at https://api.crawl4ai.com/ (the dashboard: https://api.crawl4ai.com/dashboard/).

Then send this one line to Cursor. Put your own key after `key:`.

```
set up crawl4ai - https://crawl4ai.com/llms.txt with key: <your key>
```

The agent reads the setup steps from that file and adds the Crawl4AI MCP server to its own config.

To do it by hand, add this to `mcpServers` in `~/.cursor/mcp.json`:

```json
"crawl4ai": { "url": "https://api.crawl4ai.com/mcp", "headers": { "Authorization": "Bearer <your key>" } }
```

Restart Cursor if the tools do not show.
