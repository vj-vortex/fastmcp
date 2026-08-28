import asyncio
from fastmcp import Client

# Note: In FastMCP 3 HTTP mode, the endpoint is /mcp/
client = Client("http://127.0.0.1:8000/mcp/")

async def call_tool(name: str):
    async with client:
        # Calling the 'greeting' tool defined on the server
        result = await client.call_tool("greeting", {"name": name})
        print("Result:", result)

if __name__ == "__main__":
    asyncio.run(call_tool("Ford"))