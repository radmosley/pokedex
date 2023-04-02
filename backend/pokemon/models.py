from django.db import models

# Create your models here.
class PokemonType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# # TODO: Add move effects model
# class MoveEffects(models.Model):
#     pass

# # TODO Add pokemon abilities
class PokemonAbility(models.Model):
    ability_id = models.IntegerField(primary_key=True)
    ability_name = models.CharField(max_length=200)
    ability_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ability_name

class PokemonMove(models.Model):
    move_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    power = models.IntegerField(null=True, blank=True)
#     level_learned = models.IntegerField()
#     accuracy = models.IntegerField()
#     effect_chance = models.IntegerField()
#     effect = models.ManyToManyField(MoveEffects, related_name='effect')
#     pp = models.IntegerField()
#     priority = models.IntegerField()
#     type = models.ManyToManyField(PokemonType, related_name='move_type')
    
    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front_default = models.CharField(max_length=200)
    image_front_shiny = models.CharField(max_length=200)
    hp = models.IntegerField()
    types = models.ManyToManyField(PokemonType, related_name='types')
    abilities = models.ManyToManyField(PokemonAbility, related_name='abilities')
    possible_moves = models.ManyToManyField(PokemonMove, related_name='possible_moves')

    def __str__(self):
        return self.name

