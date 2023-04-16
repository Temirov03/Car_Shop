from rest_framework import serializers
from .models import BMW,Captiva

class BMWSerializer(serializers.ModelSerializer):


    class Meta:
        model = BMW
        fields = '__all__'


class CaptivaSerializer(serializers.ModelSerializer):



    class Meta:
        model = Captiva
        fields = '__all__'