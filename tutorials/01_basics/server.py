from fastmcp import FastMCP

# Initialize FastMCP Server with a name
mcp = FastMCP("01-Basics-Server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    """
    return a + b

@mcp.tool()
def greet_user(name: str, uppercase: bool = False) -> str:
    """Return a personalized greeting.
    
    Args:
        name: Name of the person to greet
        uppercase: If true, returns greeting in uppercase
    """
    msg = f"Hello, {name}! Welcome to FastMCP."
    return msg.upper() if uppercase else msg

if __name__ == "__main__":
    # In FastMCP, run() with transport='http' defaults to serving on port 8000
    mcp.run(transport="http", port=8001)
