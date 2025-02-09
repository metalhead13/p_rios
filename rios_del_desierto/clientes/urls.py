from django.urls import path
from .views import index, buscar_cliente_por_documento, reporte_fidelizacion

urlpatterns = [
    path('', index, name='index'),
    path('api/clientes/<str:numero_documento>/', buscar_cliente_por_documento, name='buscar-cliente'),
    path('api/reporte_fidelizacion/', reporte_fidelizacion, name='reporte_fidelizacion'),
]