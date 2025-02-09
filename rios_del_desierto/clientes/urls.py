from django.urls import path
from .views import buscar_cliente_por_documento

urlpatterns = [
    path('api/clientes/<str:numero_documento>/', buscar_cliente_por_documento, name='buscar-cliente'),
]