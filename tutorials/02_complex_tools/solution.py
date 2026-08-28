from pydantic import BaseModel, EmailStr, Field
from fastmcp import FastMCP

mcp = FastMCP("User-Management-Server")

class UserProfile(BaseModel):
    username: str = Field(min_length=3, max_length=20, description="Unique username")
    email: str = Field(description="User contact email address")
    age: int = Field(ge=18, description="User age, must be at least 18")
    roles: list[str] = Field(default=["user"], description="Assigned roles")

class RegistrationResult(BaseModel):
    user_id: str
    message: str
    user: UserProfile

@mcp.tool()
def register_user(user: UserProfile) -> RegistrationResult:
    """Register a new user account with validated personal profile."""
    assigned_id = f"usr_{abs(hash(user.username)) % 10000}"
    return RegistrationResult(
        user_id=assigned_id,
        message=f"User {user.username} registered successfully!",
        user=user
    )

if __name__ == "__main__":
    mcp.run(transport="http", port=8002)
