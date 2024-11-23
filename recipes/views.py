from django.shortcuts import render
#from .models import Recipe
#from .models import load_json_to_model
import json


# views.py
from django.http import JsonResponse

recipes = [
    {
        "recipeId": 1,
        "title": "Spaghetti",
        "description": "Classic spaghetti recipe.",
        "ingredients": ["Pasta", "Tomato Sauce", "Cheese"],
        "steps": ["Boil water", "Cook pasta", "Add sauce"],
    }
]

#def recipe_list(request):
 #   return JsonResponse(recipes, safe=False)


# Create your views here.
# In your view or wherever you need to access the data:
#load_json_to_model('recipes/data/recipeData.json')
# Get all recipes
#all_recipes = Recipe.objects.all()

# Get a single recipe by ID
#single_recipe = Recipe.objects.get(recipeId=101)  # Replace 1 with your desired ID
#print(single_recipe)
# Access the JSON fields (ingredients and steps)
# For a single recipe:
#ingredients_list = single_recipe.ingredients  # This will give you the JSON data as a Python list/dict
#steps_list = single_recipe.steps

# Example usage:
def recipe_detail(request):


    data = json.load(recipes)
    for item in data:
        title = data["title"]
        description=data["description"]
    print(title)
    # Access fields
    #title = recipe.title
    #description = recipe.description
    #ingredients = recipe.ingredients  # This is your JSON data
    #steps = recipe.steps            # This is your JSON data
    #recipeType = recipe.recipeType
    
    return render(request, 'template.html', {
        "title": title,
        "description": description
        
    })

