from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        Ingredient,
        related_name = 'recipe',
        on_delete=models.CASCADE
    )

    recipe = models.ForeignKey(
        Recipe,
        related_name = 'ingredients',
        on_delete=models.CASCADE
    )
