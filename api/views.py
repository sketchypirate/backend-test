from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PlanetSerializer
from .models import Planet

class PlanetView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PlanetSerializer
    
    def get_queryset(self):
        return Planet.objects.all()
    