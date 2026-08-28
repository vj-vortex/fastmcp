"""
Exercise 3: Custom Resource Providers

Task:
1. Create a FastMCP server named "Database-Resource-Server".
2. Store a dictionary of tables:
   - "users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
   - "orders": [{"id": 101, "total": 45.0}, {"id": 102, "total": 120.0}]
3. Expose two resources:
   - `schema://tables`: Returns a list of all table names as JSON.
   - `db://tables/{table_name}`: Returns the JSON array for the specified table,
     or an error message if the table doesn't exist.
"""

from fastmcp import FastMCP

mcp = FastMCP("Database-Resource-Server")

# TODO: Implement resources schema://tables and db://tables/{table_name}

if __name__ == "__main__":
    mcp.run(transport="http", port=8003)
