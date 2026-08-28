from fastmcp import FastMCP

mcp = FastMCP("04-Prompts-Server")

# 1. Simple parameterized prompt
@mcp.prompt()
def code_explainer(code: str, language: str = "python") -> str:
    """Generate a prompt asking the model to explain code step-by-step."""
    return f"""Please explain the following {language} code snippet clearly and thoroughly:

```{language}
{code}
```

Break your explanation down into:
1. High-level purpose
2. Step-by-step logic
3. Potential edge cases or performance considerations
"""

# 2. Multi-turn system prompt builder
@mcp.prompt()
def debug_assistant(error_message: str, stack_trace: str = "") -> str:
    """Prepare a debugging session prompt."""
    prompt = f"I encountered this error:\n`{error_message}`\n\n"
    if stack_trace:
        prompt += f"Stack Trace:\n```\n{stack_trace}\n```\n\n"
    prompt += "Help me diagnose the root cause and propose a minimal fix."
    return prompt

if __name__ == "__main__":
    mcp.run(transport="http", port=8004)
