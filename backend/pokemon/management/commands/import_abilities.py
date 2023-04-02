from django.core.management.base import BaseCommand
from pokemon.models import PokemonAbility, PokemonType
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        f = open('./raw_data/abilities/abilities.json')
        poke_abilities = json.load(f)
        for ability in poke_abilities:
            ability_id = ability['effect_id']
            ability_name = ability['effect_name']
            if ability['effect_description'] != None:
                ability_description = ability['effect_description']
            else:
                ability_description = ''

            pokemon_ability = PokemonAbility.objects.get_or_create(
                ability_id = ability_id,
                ability_name = ability_name,
                ability_description = ability_description,
            )
            # Assign abilities to pokemon
            print(ability_name + ' created')