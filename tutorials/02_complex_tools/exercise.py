"""
Exercise 2: Pydantic Validation & User Registration

Task:
1. Create a FastMCP server named "User-Management-Server".
2. Define a Pydantic model `UserProfile`:
   - `username`: str (min length 3, max length 20)
   - `email`: str
   - `age`: int (ge=18)
   - `roles`: list[str] (default ["user"])
3. Create a tool `register_user(user: UserProfile) -> dict` that simulates saving the user
   and returns a confirmation message with an assigned `user_id`.
"""

from pydantic import BaseModel, Field
from fastmcp import FastMCP

mcp = FastMCP("User-Management-Server")

# TODO: Define UserProfile model and register_user tool

if __name__ == "__main__":
    mcp.run(transport="http", port=8002)
