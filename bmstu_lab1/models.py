from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Ingredient(models.Model):
    """Таблица ингредиентов для кофе"""
    name = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Цена"
    )
    unit = models.CharField(max_length=20, verbose_name="Единица измерения")
    description = models.TextField(verbose_name="Описание")
    image_url = models.URLField(null=True, blank=True, verbose_name="URL изображения")
    is_active = models.BooleanField(default=True, verbose_name="Действует")

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.name


class CoffeeRecipe(models.Model):
    """Таблица рецептов кофе (услуг)"""
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="Действует")
    image_url = models.URLField(null=True, blank=True, verbose_name="URL изображения")
    base_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Базовая цена"
    )

    class Meta:
        verbose_name = "Рецепт кофе"
        verbose_name_plural = "Рецепты кофе"

    def __str__(self):
        return self.name


class Order(models.Model):
    """Таблица заявок на приготовление кофе"""
    DRAFT = 'draft'
    DELETED = 'deleted'
    FORMED = 'formed'
    COMPLETED = 'completed'
    REJECTED = 'rejected'

    STATUS_CHOICES = [
        (DRAFT, 'Черновик'),
        (DELETED, 'Удалён'),
        (FORMED, 'Сформирован'),
        (COMPLETED, 'Завершён'),
        (REJECTED, 'Отклонён'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=DRAFT,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    formed_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата формирования")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата завершения")
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name="Создатель"
    )
    moderator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='moderated_orders',
        verbose_name="Модератор"
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Итоговая цена"
    )
    special_requests = models.TextField(
        blank=True,
        verbose_name="Особые пожелания"
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        constraints = [
            models.UniqueConstraint(
                fields=['creator', 'status'],
                condition=models.Q(status='draft'),
                name='unique_draft_per_user'
            )
        ]

    def __str__(self):
        return f"Заявка #{self.id} - {self.get_status_display()}"

    def calculate_total(self):
        """Расчет итоговой цены при завершении заявки"""
        self.total_price = sum(
            item.quantity * item.ingredient.price
            for item in self.items.all()
        )
        self.save()


class OrderItem(models.Model):
    """Связь M-M между заявками и ингредиентами"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Заявка"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        verbose_name="Ингредиент"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    is_main = models.BooleanField(default=False, verbose_name="Основной ингредиент")
    order_in_recipe = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Порядок добавления"
    )

    class Meta:
        verbose_name = "Позиция заявки"
        verbose_name_plural = "Позиции заявок"
        unique_together = [['order', 'ingredient']]

    def __str__(self):
        return f"{self.ingredient} x{self.quantity} в заявке #{self.order_id}"