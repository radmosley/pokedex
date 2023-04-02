from django.core.management.base import BaseCommand
from pokemon.models import PokemonMove, PokemonType, Pokemon
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        f = open('./raw_data/moves/final/moves_300.json')
        poke_moves = json.load(f)
        for move in poke_moves:
            move_id = move['move_id']
            move_name = move['move_name']
            if move['move_power'] != None:
                move_power = move['move_power']
            else:
                move_power = 0

            pokemon_move = PokemonMove.objects.get_or_create(
                move_id = move_id,
                name = move_name,
                power = move_power,
                # level_learned = move_level_learned,
            )
            # Assign move type
            # for p_types in pokemon['']
            # Assign ability to pokemon
            # pokemon = Pokemon.objects.get(name = pokemon)
            # pokemon.abilities.add(pokemon_move)