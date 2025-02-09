from django.db import models

class TipoDocumento(models.Model):
    """
    Tabla que almacena tipos de documentos.
    """
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    """
    Tabla que almacena la información.
    """
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    # Se pueden agregar más campos si se requiere (dirección, ciudad, etc.)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.numero_documento}"

class Compra(models.Model):
    """
    Tabla que almacena información de las compras.
    """
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='compras')
    fecha_compra = models.DateTimeField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Compra de {self.cliente.nombre} {self.cliente.apellido} por ${self.monto} el {self.fecha_compra}"