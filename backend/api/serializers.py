# add serializers for your api views


from rest_framework import serializers
from pokemon.models import Pokemon, PokemonType, PokemonAbility, PokemonMove

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = PokemonType

class NestedAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('ability_name',)
        model = PokemonAbility

class NestedMoveSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = PokemonMove

class PokemonSerializer(serializers.ModelSerializer):
    type_info = NestedTypeSerializer(many=True, source='types')
    ability_info = NestedAbilitySerializer(many=True, source='abilities')
    move_info = NestedMoveSerializer(many=True, source='possible_moves')
    class Meta:
        fields = ('number', 'name', 'ability_info', 'height', 'weight', 'image_front_default', 'image_front_shiny', 'type_info', 'hp', 'move_info')
        model = Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = PokemonType

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('ability_name',)
        model = PokemonAbility

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = PokemonMove