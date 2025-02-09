from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['numero_documento', 'nombre', 'apellido', 'correo', 'telefono']