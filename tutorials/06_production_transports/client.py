import asyncio
from fastmcp import Client

# Testing against HTTP transport endpoint
client = Client("http://127.0.0.1:8006/mcp/")

async def main():
    async with client:
        info = await client.call_tool("get_system_info")
        print("=== System Info from Production Server ===")
        print(info)

if __name__ == "__main__":
    asyncio.run(main())
