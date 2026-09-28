# Crawl4AI Cloud for Codex

A plugin for Codex is coming soon.

## Use it today

Get an API key at https://crawl4ai.com (the dashboard: https://crawl4ai.com/dashboard/).

Then send this one line to Codex. Put your own key after `key:`.

```
set up crawl4ai - https://crawl4ai.com/llms.txt with key: <your key>
```

The agent reads the setup steps from that file and adds the Crawl4AI MCP server to its own config.

To do it by hand, add this to `~/.codex/config.toml`:

```toml
[mcp_servers.crawl4ai]
url = "https://api.crawl4ai.com/mcp"
http_headers = { Authorization = "Bearer <your key>" }
```

Restart Codex if the tools do not show.
