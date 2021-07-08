from .models import Marca, Rams
from rest_framework import serializers


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Marca
        fields ='__all__'

class RamsSerializer(serializers.ModelSerializer):
    nombre_marca =serializers.CharField(read_only=True, source="Marca.nombre")
    Marca= MarcaSerializer(read_only=True)
    nombre = serializers.CharField(required=True, min_length=3)

    class Meta:
        model = Rams
        fields = '__all__'
