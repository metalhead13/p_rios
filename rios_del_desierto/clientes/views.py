# clientes/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente
from .serializers import ClienteSerializer

from django.shortcuts import render 

def index(request):
        return render(request, 'index.html')


@api_view(['GET'])
def buscar_cliente_por_documento(request, numero_documento):
    try:
        cliente = Cliente.objects.get(numero_documento=numero_documento)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data, status=200)
    except Cliente.DoesNotExist:
        return Response({"error": "Cliente no encontrado."}, status=404)