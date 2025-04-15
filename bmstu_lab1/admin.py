from django.contrib import admin
from .models import CoffeeRecipe, Ingredient, Order, OrderItem

@admin.register(CoffeeRecipe)
class CoffeeRecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_price', 'is_active')  # Только существующие поля
    list_filter = ('is_active',)  # Только существующие поля
    search_fields = ('name', 'description')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'unit', 'is_active')
    list_filter = ('is_active', 'unit')
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'creator', 'created_at')
    list_filter = ('status',)
    search_fields = ('creator__username', 'special_requests')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'ingredient', 'quantity', 'is_main')
    list_filter = ('is_main',)