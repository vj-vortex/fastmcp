import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8005/mcp/")

async def main():
    async with client:
        print("=== Calling process_batch tool ===")
        items_to_process = ["data_file_1.csv", "image_render.png", "report_q3.pdf"]
        
        result = await client.call_tool("process_batch", {"items": items_to_process})
        print("\n=== Result Received ===")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
