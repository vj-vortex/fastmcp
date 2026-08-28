import os
import sys
from fastmcp import FastMCP

# In production, you can select transport mode via environment variable or argument:
# - stdio: Default transport for local desktop clients (Claude Desktop, Cursor, CLI)
# - http: SSE/HTTP transport for remote or distributed microservices

mcp = FastMCP("06-Production-Server")

@mcp.tool()
def get_system_info() -> dict:
    """Return environment and runtime execution metadata."""
    return {
        "platform": sys.platform,
        "python_version": sys.version,
        "pid": os.getpid(),
        "cwd": os.getcwd()
    }

if __name__ == "__main__":
    transport = os.getenv("MCP_TRANSPORT", "stdio").lower()
    
    if transport == "http":
        print("Starting FastMCP server with HTTP transport on port 8006...", file=sys.stderr)
        mcp.run(transport="http", port=8006)
    else:
        # Defaults to standard I/O (stdio) for Claude Desktop and Antigravity
        mcp.run()
