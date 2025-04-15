from django.urls import path
from bmstu_lab1 import views

urlpatterns = [
    path("", views.ingredients_list, name="ingredients_list"),
    path("ingredient/<int:ingredient_id>/", views.ingredient_detail, name="ingredient_detail"),
    path("recipe/", views.recipe_detail, name="recipe_detail"),
    path("add-to-recipe/<int:ingredient_id>/", views.add_to_recipe, name="add_to_recipe"),
]
