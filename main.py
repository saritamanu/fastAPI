from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Recipe(BaseModel):
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    imageUrl: Optional[str] = None
    
recipes = []

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/recipes/")
def create_recipe(recipe: Recipe):
    recipes.append(recipe)
    return {"message": "Recipe created successfully", "recipe": recipe}

@app.get("/recipes/", response_model=List[Recipe])
def get_recipe():
    return recipes
    