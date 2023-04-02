from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):

    def handle(self, *args, **options):
        pokemon_range = 1281
        for pokemon in range(500 ,600):
            url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon)
            response = requests.request("GET", url)
            # json_object = json.load(response.text)
            with open('./raw_data/pokemon/pokemon_'+ str(pokemon) + '.json', 'w') as savefile:
                savefile.write(response.text)
                print('saving pokemon ' + str(pokemon))