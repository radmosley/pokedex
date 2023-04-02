from django.contrib import admin
from .models import Pokemon, PokemonType, PokemonMove, PokemonAbility

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(PokemonType)
admin.site.register(PokemonMove)
admin.site.register(PokemonAbility)