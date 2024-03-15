from django.shortcuts import render
from django.http import HttpResponse
from ledger.models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return HttpResponse('Recipe Book Ledger')

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'

    
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'

