import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8003/mcp/")

async def main():
    async with client:
        # 1. List available resources
        resources = await client.list_resources()
        print("=== Available Resources ===")
        for res in resources:
            print(f"- {res.uri}: {res.name} ({res.description})")

        # 2. Read static resource
        metrics = await client.read_resource("system://metrics")
        print("\n=== Read system://metrics ===")
        print(metrics)

        # 3. Read dynamic resource
        doc = await client.read_resource("docs://topics/getting-started")
        print("\n=== Read docs://topics/getting-started ===")
        print(doc)

if __name__ == "__main__":
    asyncio.run(main())
