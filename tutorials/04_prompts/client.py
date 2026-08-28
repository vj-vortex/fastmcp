import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8004/mcp/")

async def main():
    async with client:
        # 1. List available prompts
        prompts = await client.list_prompts()
        print("=== Available Prompts ===")
        for p in prompts:
            print(f"- {p.name}: {p.description}")

        # 2. Get rendered prompt
        rendered = await client.get_prompt(
            "code_explainer",
            {"code": "def fib(n):\n    return n if n <= 1 else fib(n-1) + fib(n-2)", "language": "python"}
        )
        print("\n=== Rendered Prompt ===")
        print(rendered)

if __name__ == "__main__":
    asyncio.run(main())
