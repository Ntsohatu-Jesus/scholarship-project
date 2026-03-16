from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

items = []

# Item model with validation
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

# Filter items by category or price
@app.get("/items")
def get_items(category: str = None, max_price: float = None):

    filtered = items

    if category:
        filtered = [i for i in filtered if i.category == category]

    if max_price:
        filtered = [i for i in filtered if i.price <= max_price]

    return filtered

# Statistics endpoint
@app.get("/stats")
def stats():

    total_items = len(items)

    total_value = sum(
        i.price * i.quantity for i in items
    )

    most_expensive = None
    if items:
        most_expensive = max(items, key=lambda x: x.price)

    return {
        "total_items": total_items,
        "inventory_value": total_value,
        "most_expensive_item": most_expensive
    }