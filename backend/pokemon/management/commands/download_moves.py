from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):

    def handle(self, *args, **options):
        move_range = 920
        for move in range(move_range):
            url = "https://pokeapi.co/api/v2/move/" + str(move)
            response = requests.request("GET", url)
            # json_object = json.load(response.text)
            with open('./raw_data/moves/moves_'+ str(move) + '.json', 'w') as savefile:
                savefile.write(response.text)
                print('saving move ' + str(move))