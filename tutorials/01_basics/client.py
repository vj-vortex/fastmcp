import asyncio
from fastmcp import Client

# FastMCP 3.x HTTP transport endpoint is at /mcp/
client = Client("http://127.0.0.1:8001/mcp/")

async def main():
    async with client:
        # 1. List available tools from the server
        tools = await client.list_tools()
        print("=== Available Tools ===")
        for tool in tools:
            print(f"- {tool.name}: {tool.description}")
        
        # 2. Call 'add' tool
        add_result = await client.call_tool("add", {"a": 12.5, "b": 7.5})
        print("\n=== Call 'add' result ===")
        print("Result:", add_result)

        # 3. Call 'greet_user' tool
        greet_result = await client.call_tool("greet_user", {"name": "Alice", "uppercase": True})
        print("\n=== Call 'greet_user' result ===")
        print("Result:", greet_result)

if __name__ == "__main__":
    asyncio.run(main())
