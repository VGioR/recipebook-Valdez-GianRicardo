from datetime import datetime
from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Ingredient: {}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse("Ingredient_detail", args=[str(self.name)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Recipe: {}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse("Recipe_detail", args=[str(self.name)])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name='Ingredients'
    )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='Recipes'
    )