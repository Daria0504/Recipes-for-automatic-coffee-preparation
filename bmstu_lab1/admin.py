from django.contrib import admin
from .models import CoffeeRecipe

@admin.register(CoffeeRecipe)
class CoffeeRecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'milk_ml', 'espresso_ml')
    search_fields = ('name', 'description')
    list_filter = ('vanilla_syrup_tsp', 'cinnamon_tsp')