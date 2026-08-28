from fastmcp import FastMCP

mcp = FastMCP("Calculator-Server")

@mcp.tool()
def calculate(a: float, b: float, operation: str = "add") -> float:
    """Perform a basic mathematical calculation on two numbers.
    
    Args:
        a: The first operand.
        b: The second operand.
        operation: Math operation to perform ('add', 'subtract', 'multiply', 'divide').
    """
    op = operation.lower().strip()
    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Unknown operation '{operation}'. Supported: add, subtract, multiply, divide")

if __name__ == "__main__":
    mcp.run(transport="http", port=8001)
