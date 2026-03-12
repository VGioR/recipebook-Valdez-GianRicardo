from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile, User, RecipeImage
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]


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

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage

    fieldsets = [
        ('Details', {
            'fields': ['recipe_image', 'description', 'recipe']
        }),
    ]




admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Ingredient)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
