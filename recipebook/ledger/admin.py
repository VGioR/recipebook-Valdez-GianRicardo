from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    search_fields = ('ingredient_', )
    list_display = ('ingredient', 'quantity', 'recipe')
    list_filter = ('recipe', )
    fieldsets = [
        ('Details', {
            'fields': ['ingredient', 'quantity', 'recipe']
        }),
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Ingredient)
admin.site.register(Profile, ProfileAdmin)
