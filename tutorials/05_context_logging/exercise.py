"""
Exercise 5: Context Telemetry & Diagnostics

Task:
1. Create a FastMCP server named "Diagnostics-Server".
2. Implement a tool `run_diagnostics(checks: list[str], ctx: Context)`:
   - For each check, send an `info` log message.
   - If any check name starts with "warn_", emit a `warning` log message using `ctx.warning(...)`.
   - Update `ctx.report_progress(...)` at each iteration.
   - Return a summary of passed and warned checks.
"""

from fastmcp import Context, FastMCP

mcp = FastMCP("Diagnostics-Server")

# TODO: Implement run_diagnostics tool with Context parameter

if __name__ == "__main__":
    mcp.run(transport="http", port=8005)
