import asyncio
from fastmcp import Context, FastMCP

mcp = FastMCP("05-Context-Logging-Server")

@mcp.tool()
async def process_batch(items: list[str], ctx: Context) -> dict:
    """Process a batch of items with real-time logs and progress tracking.
    
    Args:
        items: List of item names to process
        ctx: Injected FastMCP Context object
    """
    total = len(items)
    await ctx.info(f"Received batch job with {total} items")
    
    processed = []
    for i, item in enumerate(items, start=1):
        # Report progress back to client
        await ctx.report_progress(progress=i, total=total)
        await ctx.debug(f"Processing item {i}/{total}: {item}")
        
        await asyncio.sleep(0.2)  # Simulate asynchronous work
        processed.append(item.upper())
        
    await ctx.info("Batch processing completed successfully.")
    return {
        "status": "completed",
        "count": total,
        "results": processed
    }

if __name__ == "__main__":
    mcp.run(transport="http", port=8005)
