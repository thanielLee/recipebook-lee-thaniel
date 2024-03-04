from django.shortcuts import render
from django.http import HttpResponse
from ledger.models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def index(request):
    return HttpResponse('Recipe Book Ledger')

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'

    
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'

