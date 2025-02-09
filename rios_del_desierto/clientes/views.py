# clientes/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Compra
from .serializers import ClienteSerializer

from django.shortcuts import render 

import pandas as pd
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta


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
    
    
    
def reporte_fidelizacion(request):
    """
    Genera un reporte en Excel con los clientes que superen 5.000.000 COP 
    en el último mes.
    """
    hoy = timezone.now()
    hace_un_mes = hoy - timedelta(days=30)

    # Obtener compras del último mes
    compras_ultimo_mes = Compra.objects.filter(fecha_compra__gte=hace_un_mes)

    # Construimos una lista para crear un DataFrame
    data_compras = []
    for compra in compras_ultimo_mes:
        data_compras.append({
            'cliente_id': compra.cliente.id,
            'monto': float(compra.monto),  # Convertir de Decimal a float
        })

    # Crear DataFrame (puede estar vacío si no hay compras)
    df = pd.DataFrame(data_compras)

    if not df.empty:
        # Agrupar por cliente y sumar montos
        df_agrupado = df.groupby('cliente_id').sum().reset_index()
        # Filtrar quienes superen 5.000.000
        df_filtrado = df_agrupado[df_agrupado['monto'] > 5000000]

        # Recuperar información de esos clientes
        clientes_id = df_filtrado['cliente_id'].tolist()
        clientes_fidelizar = Cliente.objects.filter(id__in=clientes_id)

        # Armar DataFrame final
        reporte_data = []
        for cli in clientes_fidelizar:
            total_monto = df_filtrado.loc[
                df_filtrado['cliente_id'] == cli.id, 'monto'
            ].values[0]
            reporte_data.append({
                'NumeroDocumento': cli.numero_documento,
                'Nombre': cli.nombre,
                'Apellido': cli.apellido,
                'Correo': cli.correo,
                'Telefono': cli.telefono,
                'MontoUltimoMes': total_monto
            })

        df_reporte = pd.DataFrame(reporte_data)
    else:
        # Si no hubo compras en el último mes, retornamos un df vacío con las columnas esperadas
        df_reporte = pd.DataFrame(columns=[
            'NumeroDocumento', 'Nombre', 'Apellido', 'Correo', 'Telefono', 'MontoUltimoMes'
        ])

    # Generar el archivo Excel en memoria
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    # Nombre sugerido para el archivo
    response['Content-Disposition'] = 'attachment; filename=reporte_fidelizacion.xlsx'

    # Usar pd.ExcelWriter para escribir el DataFrame en el response
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df_reporte.to_excel(writer, index=False, sheet_name='Fidelizacion')

    return response