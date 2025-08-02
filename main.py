from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
import json
import os

app = FastAPI(
    title="Restaurants API",
    description="A collaborative list of top restaurants to try in France.",
    version="1.0.0"
)

DATA_FILE = "data.json"

# Pydantic model
class Restaurant(BaseModel):
    id: int
    name: str
    city: str
    cuisine: str
    rating: float = Field(..., ge=0, le=5)

# Load JSON
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Save JSON
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.get("/restaurants", response_model=List[Restaurant])
def list_restaurants(city: Optional[str] = None, cuisine: Optional[str] = None, min_rating: Optional[float] = None):
    data = load_data()
    if city:
        data = [r for r in data if r["city"].lower() == city.lower()]
    if cuisine:
        data = [r for r in data if r["cuisine"].lower() == cuisine.lower()]
    if min_rating:
        data = [r for r in data if r["rating"] >= min_rating]
    return data

@app.get("/restaurants/{restaurant_id}", response_model=Restaurant)
def get_restaurant(restaurant_id: int):
    data = load_data()
    for r in data:
        if r["id"] == restaurant_id:
            return r
    raise HTTPException(status_code=404, detail="Restaurant not found")

@app.post("/restaurants")
def add_restaurant(restaurant: Restaurant):
    data = load_data()
    if any(r["id"] == restaurant.id for r in data):
        raise HTTPException(status_code=400, detail="Restaurant ID already exists")
    data.append(restaurant.dict())
    save_data(data)
    return {"message": "Restaurant added successfully"}

@app.put("/restaurants/{restaurant_id}")
def update_restaurant(restaurant_id: int, updated: Restaurant):
    data = load_data()
    for i, r in enumerate(data):
        if r["id"] == restaurant_id:
            data[i] = updated.dict()
            save_data(data)
            return {"message": "Restaurant updated successfully"}
    raise HTTPException(status_code=404, detail="Restaurant not found")

@app.delete("/restaurants/{restaurant_id}")
def delete_restaurant(restaurant_id: int):
    data = load_data()
    new_data = [r for r in data if r["id"] != restaurant_id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Restaurant not found")
    save_data(new_data)
    return {"message": "Restaurant deleted successfully"}

