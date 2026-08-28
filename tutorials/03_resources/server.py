import json
from fastmcp import FastMCP

mcp = FastMCP("03-Resources-Server")

# In-memory mock database
MOCK_DOCUMENTS = {
    "getting-started": "# Getting Started with MCP\n\nMCP standardizes tool and resource integrations.",
    "architecture": "# Architecture\n\nFastMCP sits between the LLM client and your application APIs.",
    "faq": "# Frequently Asked Questions\n\nQ: Is FastMCP fast?\nA: Yes, it is built for low latency."
}

# 1. Static Resource: Fixed URI endpoint
@mcp.resource("system://metrics")
def get_system_metrics() -> str:
    """Returns current system health and status metrics."""
    return json.dumps({
        "status": "healthy",
        "uptime_seconds": 3600,
        "active_connections": 12
    })

# 2. Dynamic Resource Template: URI with parameters
@mcp.resource("docs://topics/{slug}")
def get_documentation(slug: str) -> str:
    """Retrieve documentation article by topic slug."""
    if slug not in MOCK_DOCUMENTS:
        return f"Error: Documentation topic '{slug}' not found. Available: {list(MOCK_DOCUMENTS.keys())}"
    return MOCK_DOCUMENTS[slug]

if __name__ == "__main__":
    mcp.run(transport="http", port=8003)
