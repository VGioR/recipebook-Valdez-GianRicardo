from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def recipe_list(request):
	recipes = Recipe.objects.all()
	ctx = {"recipes" : recipes}
	return render(request, 'recipe_list.html', ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {"recipe" : recipe}

    return render(request, 'recipe.html', ctx)
