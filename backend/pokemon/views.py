from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Pokemon
# Create your views here.
# def index(request):
#     pokemon = Pokemon.objects.all()
#     return render(request, 'index.html', {'pokemon':pokemon})

class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = 'pokemon/pokemon_detail.html'
    context_object_name = 'pokemon'

def throw_pokeball(request):
    pass