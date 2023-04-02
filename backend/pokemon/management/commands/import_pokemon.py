from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from pokemon.models import Pokemon, PokemonType, PokemonMove, PokemonAbility
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Pokemon.objects.all().delete()
        versions = ['150', '300']
        f = open('./raw_data/pokemon/final/pokemon_150.json')
        poke_balls = json.load(f)
        for pokemon in poke_balls:
            name_ext = pokemon.get('name')
            number_ext = int(pokemon.get('number'))
            height_ext = int(pokemon.get('height'))
            weight_ext = int(pokemon.get('weight'))
            if pokemon['image_front_default'] != None:
                image_front_default = pokemon.get('image_front_default')
            else:
                image_front_default = ''
            if pokemon['image_front_shiny'] != None:
                image_front_shiny = pokemon.get('image_front_shiny')
            else:
                image_front_default = ''
            if pokemon['hp'] != None:
                hp = int(pokemon.get('hp'))
            else:
                hp = 0

            pokemon_obj = Pokemon.objects.create(
                name = name_ext,
                number = number_ext,
                height = height_ext,
                weight = weight_ext,
                image_front_default = image_front_default,
                image_front_shiny = image_front_shiny,
                hp = hp,
            )
# Assign types
            for p_types in pokemon['types']:
                pokemon_type, created = PokemonType.objects.get_or_create(name=p_types)
                pokemon_obj.types.add(pokemon_type)

# Assign abilities
            for p_ability in pokemon['abilities']:
                pokemon_ability = PokemonAbility.objects.get(
                    ability_name = p_ability
                )
                print(p_ability)
                pokemon_obj.abilities.add(pokemon_ability)
            print('____________________________')

# Assign moves
            for p_move in pokemon['moves']:
                pokemon_move = PokemonMove.objects.get(
                    name = p_move['name']
                )
                print(p_move['name'])
                pokemon_obj.possible_moves.add(pokemon_move)
            print(pokemon_obj.name + ' has been uploaded')
            print('____________________________')