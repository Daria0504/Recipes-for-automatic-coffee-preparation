from django.shortcuts import render, get_object_or_404
from .models import CoffeeRecipe

# Начальные данные для рецептов (можно заменить на загрузку из БД)
coffee_recipes = [
    {
        "id": 1,
        "name": "Ванильный латте",
        "milk_ml": 175,
        "espresso_ml": 50,
        "vanilla_syrup_tsp": 2,
        "cinnamon_tsp": 1,
        "ground_coffee_g": 15,
        "honey_g": 0,
        "description": "Нежный латте с ванильным сиропом и легкой ноткой корицы",
        "image_url": "http://127.0.0.1:3010/coffee-images/vanilla_latte.jpg"
    },
    {
        "id": 2,
        "name": "Холодный латте",
        "milk_ml": 175,
        "espresso_ml": 50,
        "vanilla_syrup_tsp": 0,
        "cinnamon_tsp": 0,
        "ground_coffee_g": 15,
        "honey_g": 5,
        "description": "Освежающий холодный латте с кубиками льда",
        "image_url": "http://127.0.0.1:3010/coffee-images/cold_latte.jpg"
    }
]


def coffee_list(request):
    search_query = request.GET.get("search", "").lower()

    if search_query:
        filtered_recipes = [r for r in coffee_recipes
                            if search_query in r["name"].lower() or
                            search_query in r["description"].lower()]
    else:
        filtered_recipes = coffee_recipes

    return render(request, "coffee/coffee_list.html", {
        "recipes": filtered_recipes,
        "search_query": search_query
    })


def coffee_detail(request, recipe_id):
    # recipe = get_object_or_404(CoffeeRecipe, id=recipe_id)
    # Или для временного решения без БД:
    recipe = next((r for r in coffee_recipes if r["id"] == recipe_id), None)
    if not recipe:
        raise Http404("Рецепт не найден")

    return render(request, "coffee/coffee_detail.html", {
        "recipe": recipe
    })
from django.shortcuts import render, redirect, get_object_or_404
from .models import CoffeeRecipe

def home(request):
    return render(request, 'home.html')

def send_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        # Обработка текста
        return render(request, 'text_received.html', {'text': text})
    return redirect('home')

def checkout(request):
    # Логика оформления заказа
    return render(request, 'checkout.html')
def cart_detail(request):
    # Логика отображения корзины (можно временно просто рендерить шаблон)
    return render(request, 'cart/detail.html')


from django.shortcuts import redirect


def cart_add(request, product_id):
    # Получаем или создаем корзину в сессии
    cart = request.session.get('cart', {})

    # Добавляем товар или увеличиваем количество
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1

    # Сохраняем корзину в сессии
    request.session['cart'] = cart

    # Перенаправляем обратно на страницу товара
    return redirect('coffee_detail', recipe_id=product_id)
def cart_detail(request):
    cart = request.session.get('cart', {})
    # Здесь можно добавить логику получения объектов товаров по ID из корзины
    return render(request, 'cart/detail.html', {'cart': cart})
