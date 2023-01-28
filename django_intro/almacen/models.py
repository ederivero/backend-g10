from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductosModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    precio = models.FloatField(null=False)
    estado = models.BooleanField(default=True, null=True)

    class Meta:
        db_table = 'productos'

    def __str__(self) -> str:
        return self.nombre

class CategoriasModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    estado = models.BooleanField(default=True, null=True)

    class Meta:
        db_table = 'categorias'

    def __str__(self) -> str:
        return self.nombre

class ProductosCategoriasModel(models.Model):
    id = models.AutoField(primary_key=True)
    producto_id = models.ForeignKey(ProductosModel, on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(CategoriasModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'productos_categorias'

class ClientesModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    apellido = models.CharField(max_length=45, null=False)
    correo = models.CharField(max_length=45, null=False)
    dni = models.CharField(max_length=8, null=False)

    class Meta:
        db_table = 'clientes'

class OrdenesModel(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45, null=False)
    observacion = models.CharField(max_length=100, null=True)
    estado = models.BooleanField(default=True, null=True)
    cliente_id = models.ForeignKey(ClientesModel, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ordenes'

class DetallesOrdenModel(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(null=False)
    producto_id = models.ForeignKey(ProductosModel, on_delete=models.CASCADE)
    orden_id = models.ForeignKey(OrdenesModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'detalles_orden'

class PagosModel(models.Model):
    id = models.AutoField(primary_key=True)
    monto = models.FloatField(null=False)
    numero_pago = models.IntegerField(null=False)
    orden_id = models.ForeignKey(OrdenesModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pagos'

class BoletasPagoModel(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45, null=False)
    total = models.FloatField(null=False)
    pago_id = models.ForeignKey(PagosModel, on_delete=models.CASCADE)

    class Metas:
        db_table = 'boletas_pago'