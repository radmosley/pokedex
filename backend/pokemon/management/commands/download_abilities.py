from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):

    def handle(self, *args, **options):
        pokemon_range = 358
        for pokemon in range(1, pokemon_range + 1):
            url = "https://pokeapi.co/api/v2/ability/" + str(pokemon)
            response = requests.request("GET", url)
            # json_object = json.load(response.text)
            with open('./raw_data/abilities/ability_'+ str(pokemon) + '.json', 'w') as savefile:
                savefile.write(response.text)
                print('saving ability ' + str(pokemon))