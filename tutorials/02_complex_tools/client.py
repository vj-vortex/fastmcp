import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8002/mcp/")

async def main():
    async with client:
        # Inspect tool schema
        tools = await client.list_tools()
        print("=== Available Tools & Schema ===")
        for tool in tools:
            print(f"Tool: {tool.name}\nDescription: {tool.description}")
            print(f"Input Schema: {tool.inputSchema}\n")

        # Submit structured payload
        payload = {
            "order": {
                "customer_id": "cust_9981",
                "items": [
                    {"product_name": "Mechanical Keyboard", "quantity": 1, "unit_price": 89.99},
                    {"product_name": "Wireless Mouse", "quantity": 2, "unit_price": 24.50}
                ],
                "priority": "express",
                "promo_code": "SAVE10"
            }
        }
        print("=== Calling process_order with Pydantic payload ===")
        result = await client.call_tool("process_order", payload)
        print("Receipt:", result)

if __name__ == "__main__":
    asyncio.run(main())
