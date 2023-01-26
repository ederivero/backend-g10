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