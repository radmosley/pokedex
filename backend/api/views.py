# create views for api endpoints
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from pokemon.models import Pokemon, PokemonType
from .serializers import PokemonSerializer, TypeSerializer

# Pokemon end points
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [AllowAny,]

    def list(self, request):
        serializer = PokemonSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        pokemon = get_object_or_404(Pokemon, number=pk)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)
   
class TypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    serializer_class = TypeSerializer
