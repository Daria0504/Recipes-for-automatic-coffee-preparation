from django.db import models

class CoffeeRecipe(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название рецепта")
    milk_ml = models.PositiveIntegerField(verbose_name="Молоко, мл")
    espresso_ml = models.PositiveIntegerField(verbose_name="Эспрессо, мл")
    vanilla_syrup_tsp = models.PositiveIntegerField(verbose_name="Ванильный сироп, ч/л")
    cinnamon_tsp = models.PositiveIntegerField(verbose_name="Корица, ч/л")
    ground_coffee_g = models.PositiveIntegerField(verbose_name="Кофе молотый, гр")
    honey_g = models.PositiveIntegerField(verbose_name="Мед, гр")
    description = models.TextField(verbose_name="Описание", blank=True)
    image_url = models.URLField(verbose_name="Ссылка на изображение", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рецепт кофе"
        verbose_name_plural = "Рецепты кофе"