from fastmcp import FastMCP

mcp = FastMCP("Review-Prompt-Server")

@mcp.prompt()
def pr_review(pr_title: str, diff_content: str, strictness: str = "normal") -> str:
    """Generate a Pull Request code review instructions prompt."""
    guidelines = {
        "lenient": "Focus solely on critical bugs, data corruption, and major security issues.",
        "normal": "Check for correctness, code style, edge cases, error handling, and test coverage.",
        "strict": "Perform an exhaustive analysis: nitpicks, micro-benchmarking considerations, type completeness, and documentation."
    }.get(strictness.lower(), "Check for correctness and general code quality.")

    return f"""# Pull Request Review: {pr_title}

Review Strictness: **{strictness.upper()}**
Guideline: {guidelines}

## Diff to Review:
```diff
{diff_content}
```

## Review Format:
1. **Summary of Changes**
2. **Key Findings / Concerns** (Categorized by: Security, Performance, Readability)
3. **Approval Status**: [APPROVE / REQUEST CHANGES / COMMENT]
"""

if __name__ == "__main__":
    mcp.run(transport="http", port=8004)
