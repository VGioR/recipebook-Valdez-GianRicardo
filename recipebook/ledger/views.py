from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, ImageForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, 'recipebook/recipe_list.html', ctx)

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {"recipe": recipe}

    return render(request, 'recipebook/recipe.html', ctx)

@login_required
def recipe_form(request):
    form = TaskForm()
    if(request.method == "POST"):
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            return redirect('ledger:recipe_detail', pk=recipe.pk)
    ctx = {
    "recipeform": form,
    }
    return render(request, 'recipebook/form.html', ctx)
@login_required
def image_form(request, pk):
    image_form = ImageForm()
    recipe = Recipe.objects.get(pk=pk)
    if(request.method == "POST"):
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('ledger:recipe_detail', pk=image.recipe.pk)
    ctx = {"image_form": image_form, "recipe": recipe}
    return render(request, 'recipebook/image_form.html', ctx)