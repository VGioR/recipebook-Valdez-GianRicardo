from django.urls import path
from .views import recipe_list, recipe_detail, recipe_form, image_form

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipe/<int:pk>', recipe_detail, name="recipe_detail"),
    path('recipe/add', recipe_form, name="recipe_form"),
    path('recipe/<int:pk>/add_image', image_form, name="image_form"),
]

app_name = "ledger"
