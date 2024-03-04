from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

class Recipe(models.Model):
    name = models.CharField(max_length=50)

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
