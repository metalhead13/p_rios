from django.urls import path
from .views import index, buscar_cliente_por_documento

urlpatterns = [
    path('', index, name='index'),
    path('api/clientes/<str:numero_documento>/', buscar_cliente_por_documento, name='buscar-cliente'),
]