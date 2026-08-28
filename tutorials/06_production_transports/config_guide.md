# 🔌 Production Deployment & Client Configuration Guide

This guide shows you how to connect your FastMCP servers to external tools, AI clients, and debuggers.

---

## 1. Connecting to Claude Desktop

Add your FastMCP server to your Claude Desktop configuration file:
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "my-fastmcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\code\\mcp",
        "run",
        "python",
        "tutorials/06_production_transports/server.py"
      ],
      "env": {
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```

---

## 2. Interactive Testing with MCP Inspector

Anthropic's official MCP Inspector lets you test tools, resources, and prompts in a browser UI:

```powershell
npx @modelcontextprotocol/inspector uv run python tutorials/06_production_transports/server.py
```

---

## 3. Running as an HTTP/SSE Microservice

For cloud hosting (Docker, Kubernetes, AWS ECS, GCP Cloud Run), use the `http` transport:

```powershell
$env:MCP_TRANSPORT="http"
uv run python tutorials/06_production_transports/server.py
```

FastMCP will bind to the specified port and expose the endpoint at `/mcp/`.
