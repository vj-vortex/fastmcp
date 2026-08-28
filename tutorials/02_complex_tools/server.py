from typing import Literal, Optional
from pydantic import BaseModel, Field
from fastmcp import FastMCP

mcp = FastMCP("02-Complex-Tools-Server")

class OrderItem(BaseModel):
    product_name: str = Field(description="Name of the product")
    quantity: int = Field(gt=0, description="Quantity to purchase, must be > 0")
    unit_price: float = Field(gt=0.0, description="Unit price per item")

class OrderRequest(BaseModel):
    customer_id: str = Field(description="Unique ID for the customer")
    items: list[OrderItem] = Field(description="List of items in the order")
    priority: Literal["standard", "express", "overnight"] = Field(
        default="standard",
        description="Shipping priority level"
    )
    promo_code: Optional[str] = Field(
        default=None,
        description="Optional promotional discount code"
    )

class OrderReceipt(BaseModel):
    order_id: str
    subtotal: float
    discount: float
    total: float
    status: str

@mcp.tool()
def process_order(order: OrderRequest) -> OrderReceipt:
    """Process a customer order with items, shipping priority, and promo code."""
    subtotal = sum(item.quantity * item.unit_price for item in order.items)
    
    # Simple discount logic
    discount = 0.0
    if order.promo_code == "SAVE10":
        discount = subtotal * 0.10
    
    total = max(0.0, subtotal - discount)
    
    return OrderReceipt(
        order_id=f"ORD-{abs(hash(order.customer_id)) % 100000}",
        subtotal=round(subtotal, 2),
        discount=round(discount, 2),
        total=round(total, 2),
        status="CONFIRMED"
    )

if __name__ == "__main__":
    mcp.run(transport="http", port=8002)
