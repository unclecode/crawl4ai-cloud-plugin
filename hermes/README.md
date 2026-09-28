# Crawl4AI Cloud for Hermes

A plugin for Hermes is coming soon.

## Use it today

Get an API key at https://crawl4ai.com (the dashboard: https://crawl4ai.com/dashboard/).

Then send this one line to Hermes. Put your own key after `key:`.

```
set up crawl4ai - https://crawl4ai.com/llms.txt with key: <your key>
```

The agent reads the setup steps from that file and adds the Crawl4AI MCP server to its own config.

To do it by hand, add a remote MCP server (streamable HTTP) with the URL `https://api.crawl4ai.com/mcp` and the header `Authorization: Bearer <your key>`.

Restart Hermes if the tools do not show.
