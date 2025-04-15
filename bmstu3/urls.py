"""
URL configuration for bmstu3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

from bmstu_lab1 import views


from django.contrib import admin
from django.urls import path
from bmstu_lab1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('coffee/', views.coffee_list, name='coffee_list'),
    path('coffee/<int:recipe_id>/', views.coffee_detail, name='coffee_detail'),
    path('sendText/', views.send_text, name='send_text'),  # Добавлен слэш
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
]
