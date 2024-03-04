from django.contrib import admin

from .models import Recipe, RecipeIngredient, Ingredient

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

    

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine,]

    search_fields = ('name',)
    list_display = ('name',)

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)