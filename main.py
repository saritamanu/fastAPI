from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

class Recipe(BaseModel):
    id: str
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
    recipe_id = str(uuid.uuid4())
    recipe_data = recipe.model_dump()
    recipe_data["id"] = recipe_id
    recipes.append(recipe_data)
    return {"message": "Recipe created successfully", "recipe": recipe_data}

@app.get("/recipes/", response_model=List[Recipe])
def get_recipe():
    return recipes

@app.get("/recipes/{recipe_id}")
def get_recipe_by_id(recipe_id:str):
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            return recipe
    return{"message" : "Recipe not found"}