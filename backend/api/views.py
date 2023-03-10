# create views for api endpoints
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from pokemon.models import Pokemon, PokemonType, Notes
from .serializers import PokemonSerializer, TypeSerializer, NoteSerializer

# Pokemon end points
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def list(self, request):
        serializer = PokemonSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        pokemon = get_object_or_404(self.queryset, pk=pk)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)
   
class TypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    serializer_class = TypeSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

# User end point