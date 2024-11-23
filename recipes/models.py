from django.db import models
import json

# Create your models here.
class Recipe(models.Model):
    recipeId = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=200)  
    description = models.TextField()  
    imagePath = models.CharField(max_length=500, blank=True, null=True)  
    ingredients = models.JSONField()  
    steps = models.JSONField()  
    recipeType = models.CharField(max_length=100)  

    def __str__(self):
        return self.title  

def load_json_to_model(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    for item in data:
        Recipe.objects.create(recipeId=item['recipeId'], title=item['title'], description=item['description'], imagePath=item['imagePath'], ingredients=item['ingredients'], steps=item['steps'], recipeType=item['recipeType'])


'''
def load_json_to_model(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    for item in data:
        Recipe.objects.create(name=item['name'], age=item['age'])


    recipeId: integer
    title: string
    description: string
    imagePath: string
    ingredients: list
    steps: list
    recipieType: string
'''