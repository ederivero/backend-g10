from django.db import models

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


