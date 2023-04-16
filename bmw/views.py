from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BMWSerializer,CaptivaSerializer
from .models import BMW,Captiva

# Create your views here.

class BMWViewSet(ModelViewSet):
    queryset = BMW.objects.all()
    serializer_class = BMWSerializer


class CaptivaViewSet(ModelViewSet):
    queryset = Captiva.objects.all()
    serializer_class = CaptivaSerializer


