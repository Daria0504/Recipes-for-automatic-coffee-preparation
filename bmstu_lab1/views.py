from django.shortcuts import render

# MinIO URL
MINIO_URL = "http://127.0.0.1:3010/coffee-ingredients"

# Коллекция ингредиентов для кофе
ingredients = [
    {"id": 1, "name": "Арабика зерно", "price": 1200, "unit": "кг", "description": "Кофейные зерна Арабики с мягким вкусом.", "image_url": f"https://avatars.mds.yandex.net/i?id=a8deb437a71ae50a2c17ef582bcb389a-5315630-images-thumbs&ref=rim&n=33&w=142&h=200"},
    {"id": 2, "name": "Робуста молотая", "price": 900, "unit": "кг", "description": "Молотая Робуста с насыщенным вкусом.", "image_url": f"https://cdn1.ozone.ru/s3/multimedia-f/6052853559.jpg"},
    {"id": 3, "name": "Сироп ваниль", "price": 350, "unit": "бутылка", "description": "Сироп для придания напитку ванильного аромата.", "image_url": f"https://cdn1.ozone.ru/s3/multimedia-j/6399741247.jpg"},
    {"id": 4, "name": "Корица молотая", "price": 150, "unit": "пакет", "description": "Ароматная корица для украшения капучино.", "image_url": f"https://avatars.mds.yandex.net/i?id=8b2ca06488a5853e3c61fc358f81c1de46ad34f3-5504402-images-thumbs&n=13"},
    {"id": 5, "name": "Молоко безлактозное", "price": 80, "unit": "литр", "description": "Нежное безлактозное молоко для латте.", "image_url": f"https://youmarket.shop/images/detailed/97/i_sagc-j1.webp"},
]

# Рецепт (словарь с id ингредиентов)
recipe = {
    1: ingredients[0]  # например, сразу есть Арабика
}

def ingredients_list(request):
    """Страница списка ингредиентов с фильтрацией и рецептом"""
    search_query = request.GET.get("search", "").strip().lower()
    filter_by = request.GET.get("filter_by", "all")

    filtered_ingredients = ingredients
    if search_query:
        filtered_ingredients = [
            i for i in ingredients
            if search_query in i["name"].lower() or search_query in str(i["price"]) or search_query in i["unit"].lower()
        ]

    if filter_by == "price":
        filtered_ingredients = sorted(filtered_ingredients, key=lambda x: x["price"])
    elif filter_by == "name":
        filtered_ingredients = sorted(filtered_ingredients, key=lambda x: x["name"].lower())

    return render(request, "./coffee/ingredients_list.html", {
        "ingredients": filtered_ingredients,
        "recipe_count": len(recipe),
        "search_query": search_query,
        "filter_by": filter_by
    })

def ingredient_detail(request, ingredient_id):
    """Страница с подробной информацией об ингредиенте"""
    item = next((i for i in ingredients if i["id"] == ingredient_id), None)
    return render(request, "./coffee/ingredient_detail.html", {"ingredient": item})

def recipe_detail(request):
    """Страница текущего рецепта (ингредиенты в рецепте)"""
    return render(request, "./coffee/recipe_detail.html", {"recipe": recipe})

def add_to_recipe(request, ingredient_id):
    """Добавление ингредиента в рецепт через POST-запрос"""
    global recipe
    if request.method == "POST":
        ingredient = next((i for i in ingredients if i["id"] == ingredient_id), None)
        if ingredient:
            recipe[ingredient_id] = ingredient  # Добавляем или заменяем ингредиент в рецепте

    return ingredients_list(request)
