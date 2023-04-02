from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        results = []
        for i in range(151,301):
            with open('./raw_data/pokemon/pokemon_' + str(i) + '.json', 'r') as format_file:
                data = json.load(format_file)
                number = data['id']
                name = data['name']
                types = []
                for type in data['types']:
                    types.append(type['type']['name'])
                height = data['height']
                weight = data['weight']
                abilities = []
                for ability in data['abilities']:
                    abilities.append(ability['ability']['name'])
                for stat in data['stats']:
                    if stat['stat']['name'] == 'hp':
                        hp = stat['base_stat']
                image_front_default = data['sprites']['front_female']
                image_front_shiny = data['sprites']['front_shiny']
                # image_back_default = data['sprites']['back_female']
                # image_back_shiny = data['sprites']['back_shiny']
                moves = []
                for move in data['moves']:
                    move_name = move['move']['name']
                    level_learned = 0
                    for level in move['version_group_details']:
                        if level['level_learned_at'] > level_learned:
                            level_learned = level['level_learned_at']
                            result = {
                                'name': move_name,
                                'level_learned': level_learned
                            }
                            moves.append(result)
                poke_info = {
                    'number': number,
                    'name': name,
                    'types': types,
                    'height': height,
                    'weight': weight,
                    'abilities': abilities,
                    'image_front_default': image_front_default,
                    'image_front_shiny': image_front_shiny,
                    'moves': moves,
                    'hp': hp,
                }
                results.append(poke_info)
                format_file.close()
        with open('./raw_data/pokemon/final/pokemon_' + '300' + '.json', 'a') as save_file:
            json.dump(results, save_file)
            save_file.close()
            print('pokemon' + str(i) + ' success')
            
