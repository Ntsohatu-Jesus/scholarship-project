from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Items Store API")

items = []

# Data model for items
class Item(BaseModel):
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)
    category: str

# Add item
@app.post("/items")
def add_item(item: Item):
    items.append(item)
    return item

# Get items with optional filters
@app.get("/items")
def get_items(category: str = None, max_price: float = None):

    result = items

    if category:
        result = [i for i in result if i.category == category]

    if max_price:
        result = [i for i in result if i.price <= max_price]

    return result

# Store statistics
@app.get("/stats")
def stats():

    total_items = len(items)

    total_value = sum(i.price * i.quantity for i in items)

    expensive = None
    if items:
        expensive = max(items, key=lambda x: x.price)

    return {
        "total_items": total_items,
        "inventory_value": total_value,
        "most_expensive": expensive
    }