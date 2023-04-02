from django.core.management.base import BaseCommand
import json
'''
Create main file to load into models.
Fields:
    - id(id): int
    - name(name): str
    - type(type): str
    - target(target['name']): str
    - power(power): int
    - power_points(pp): int
    - priority(priority): int
    - category(damage_class): str
    - description(effect_entries): str
    - accuracy(accuracy): int
    - contest combos(contest_combos): dict {use_after, use_before}
'''

class Command(BaseCommand):

    def handle(self, *args, **options):
        results = []
        # moves = 903
        for i in range(601, 903):
            with open('./raw_data/moves/moves_' + str(i) + '.json', 'r') as format_file:
                data = json.load(format_file)
                move_id = data['id']
                move_name = data['name']
                move_type = data['type']['name']
                move_target = data['target']['name']
                move_power = data['power']
                power_points = data['pp']
                priority = data['priority']
                damage_class = data['damage_class']['name']
                if len(data['effect_entries']) > 0:
                    move_description = data['effect_entries'][0]['effect']
                else: 
                    move_description = ''
                if data['meta'] is None:
                    category = ''
                    status = {}
                else:
                    category = data['meta']['category']['name']
                    status = {
                    'ailment': data['meta']['ailment']['name'],
                    'ailment_chance': data['meta']['ailment_chance']
                    }
                move_accuracy = data['accuracy']
                # contest_combos = data['contest_combos']['normal']
                # if data['contest_combos']['normal']['use_after']:
                #     contest_combos['use_after'] = data['contest_combos']['normal']['use_after']
                # if data['contest_combos']['normal']['use_before']:
                #     contest_combos['use_before'] = data['contest_combos']['normal']['use_before']
                entry = {
                    'move_id': move_id,
                    'move_name': move_name,
                    'move_type': move_type,
                    'move_target': move_target,
                    'move_power': move_power,
                    'power_points': power_points,
                    'priority': priority,
                    'category': category,
                    'damage_class': damage_class,
                    'status': status,
                    'move_description': move_description,
                    'move_accuracy': move_accuracy,
                    # 'contest_combos': contest_combos,
                }
                results.append(entry)
        with open('./raw_data/moves/final/moves_' + '903' + '.json', 'a') as save_file:
            json.dump(results, save_file)
            save_file.close()
            print('move ' + str(i) + ' success')