import asyncio
from fastmcp import Context, FastMCP

mcp = FastMCP("Diagnostics-Server")

@mcp.tool()
async def run_diagnostics(checks: list[str], ctx: Context) -> dict:
    """Run a series of system diagnostics with live reporting and warnings."""
    total = len(checks)
    passed = []
    warnings = []

    for i, check in enumerate(checks, start=1):
        await ctx.report_progress(progress=i, total=total)
        
        if check.startswith("warn_"):
            await ctx.warning(f"Check '{check}' generated a warning condition!")
            warnings.append(check)
        else:
            await ctx.info(f"Check '{check}' completed successfully.")
            passed.append(check)
            
        await asyncio.sleep(0.1)

    return {
        "status": "warning" if warnings else "healthy",
        "passed_count": len(passed),
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": warnings
    }

if __name__ == "__main__":
    mcp.run(transport="http", port=8005)
