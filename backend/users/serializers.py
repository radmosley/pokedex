from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import User

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class PlayerPokemonSerializer(serializers.ModelSerializer):
    pass

class PlayerProfileSerializer(serializers.ModelSerializer):
    pass

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attribute):
        if attribute['password'] != attribute['password2']:
            raise serializers.ValidationError({'password': 'Password fields must match'})
        return attribute

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = validated_data['password']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user