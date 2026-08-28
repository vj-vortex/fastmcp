"""
Exercise 1: Basic Tools & Math Calculator

Task:
1. Create a FastMCP server named "Calculator-Server".
2. Add a tool named `calculate` that accepts:
   - `a` (float)
   - `b` (float)
   - `operation` (str): one of "add", "subtract", "multiply", "divide"
3. Return the calculated float or raise ValueError for invalid operations or division by zero.
4. Provide clear docstrings for automatic schema reflection.
"""

from fastmcp import FastMCP

mcp = FastMCP("Calculator-Server")

# TODO: Define the @mcp.tool() here
# def calculate(a: float, b: float, operation: str = "add") -> float:
#     ...

if __name__ == "__main__":
    mcp.run(transport="http", port=8001)
