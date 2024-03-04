from django.urls import path
from .views import index, RecipeDetailView, RecipeListView

urlpatterns = [
    path('', index, name='ledger'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe_detail"),
    path('recipes/list', RecipeListView.as_view(), name="list")
]

app_name = 'ledger'