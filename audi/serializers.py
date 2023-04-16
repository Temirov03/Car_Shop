from rest_framework import serializers
from .models import Audi


class AudiSerializer(serializers.ModelSerializer):



    class Meta:
        model = Audi
        fields = '__all__'