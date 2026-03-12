from django.urls import path
from .views import recipe_list, recipe_detail, recipe_form

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipe/<int:pk>', recipe_detail, name="recipe_detail"),
    path('recipe/add', recipe_form, name="recipe_form"),
]

app_name = "ledger"
