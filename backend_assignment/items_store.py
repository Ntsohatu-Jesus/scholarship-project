from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

items = []

# Item data model with validation
class Item(BaseModel):
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)
    category: str

# Add a new item
@app.post("/items")
def add_item(item: Item):
    items.append(item)
    return {"message": "Item added", "item": item}

# Get all items
@app.get("/items")
def get_items():
    return items

# Get single item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    return {"error": "Item not found"}

# Delete item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(items):
        deleted = items.pop(item_id)
        return {"deleted": deleted}
    return {"error": "Item not found"}