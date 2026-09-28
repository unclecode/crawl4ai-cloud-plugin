# Crawl4AI Cloud for OpenClaw

A plugin for OpenClaw is coming soon.

## Use it today

Get an API key at https://api.crawl4ai.com/ (the dashboard: https://api.crawl4ai.com/dashboard/).

Then send this one line to OpenClaw. Put your own key after `key:`.

```
set up crawl4ai - https://crawl4ai.com/llms.txt with key: <your key>
```

The agent reads the setup steps from that file and adds the Crawl4AI MCP server to its own config.

To do it by hand, add this to `mcp.servers` in `~/.openclaw/openclaw.json`:

```json5
crawl4ai: { url: "https://api.crawl4ai.com/mcp", transport: "streamable-http", headers: { Authorization: "Bearer <your key>" } }
```

Restart OpenClaw if the tools do not show.
