from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        results = []
        for i in range(1, 300):
            with open('./raw_data/abilities/ability_' + str(i) + '.json', 'r') as format_file:
                data = json.load(format_file)
                effect_name = data['name']
                pokemon_w_effects = []
                effect_description = ''
                for poke in data['pokemon']:
                    pokemon_w_effects.append(poke['pokemon']['name'])
                for entry in data['effect_entries']:
                    if entry['language']['name'] == 'en':
                        effect_description = entry['effect']
                result = {
                    'effect_name': effect_name,
                    'pokemon_w_effect': pokemon_w_effects,
                    'effect_description': effect_description,
                    'effect_id': data['id']

                }
                results.append(result)
            with open('./raw_data/abilities/abilities.json', 'a') as save_file:
                json.dump(result, save_file)
                save_file.close()
                print('abilities' + str(i) + 'success')