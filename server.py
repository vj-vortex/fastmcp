from fastmcp import FastMCP


mcp = FastMCP("My Server")

@mcp.tool()
def greeting(name: str)-> str:
    return "Hello " + name

if __name__=="__main__":
    mcp.run(transport="http", port=8000)