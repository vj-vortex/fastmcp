"""
Exercise 4: Pull Request Review Prompt

Task:
1. Create a FastMCP server named "Review-Prompt-Server".
2. Add a prompt named `pr_review` that accepts:
   - `pr_title` (str)
   - `diff_content` (str)
   - `strictness` (str, default: "normal", options: "lenient", "normal", "strict")
3. Return a markdown-formatted prompt instructing an LLM to review the PR diff with specific
   focus areas (Security, Performance, Style) based on strictness.
"""

from fastmcp import FastMCP

mcp = FastMCP("Review-Prompt-Server")

# TODO: Implement pr_review prompt

if __name__ == "__main__":
    mcp.run(transport="http", port=8004)
