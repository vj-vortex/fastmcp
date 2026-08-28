import json
from fastmcp import FastMCP

mcp = FastMCP("Database-Resource-Server")

DB_TABLES = {
    "users": [
        {"id": 1, "name": "Alice", "role": "admin"},
        {"id": 2, "name": "Bob", "role": "developer"}
    ],
    "orders": [
        {"id": 101, "customer_id": 1, "total": 45.0},
        {"id": 102, "customer_id": 2, "total": 120.0}
    ]
}

@mcp.resource("schema://tables")
def list_tables() -> str:
    """Returns a list of available database tables."""
    return json.dumps(list(DB_TABLES.keys()))

@mcp.resource("db://tables/{table_name}")
def get_table_data(table_name: str) -> str:
    """Retrieve all rows for a specific database table."""
    if table_name not in DB_TABLES:
        return json.dumps({"error": f"Table '{table_name}' does not exist."})
    return json.dumps(DB_TABLES[table_name], indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", port=8003)
