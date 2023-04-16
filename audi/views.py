from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AudiSerializer
from .models import Audi

# Create your views here.

class AudiViewSet(ModelViewSet):
    queryset = Audi.objects.all()
    serializer_class = AudiSerializer