from django.db import models

class CategoriaModel(models.Model):
    # Si no especificamos la columna ID django lo hara de manera predeterminada con el tipo de dato AutoField y tbn lo colocara como llave primaria
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True) # en la bd creara un varchar con 50 caracteres de longitud maxima
    
    class Meta: 
        # sirve para definir los atributos de la clase que estamos heredando directamente para pasarle la metadata sin utilizar el metodo super
        # sirve para modificar la configuracion y comportamiento de esta tabla en la base de datos
        # https://docs.djangoproject.com/en/4.1/ref/models/options/
        db_table = 'categorias'
        # modificamos el ordenamiento al momento de devolver los registros
        # nombre ascendente (A-Z)
        # nombre descendente (Z-A)
        # como ya sabemos que el nombre jamas se repetira la segunda clausula de ordenamiento esta de mas porque nunca se va a dar
        ordering = ['nombre', 'id']


class PlatoModel(models.Model):
    # id = models.AutoField(primary_key= True, null=False)
    nombre = models.CharField(max_length=50, unique=True, null=False)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    # auto_now_add > cada vez que cree un nuevo registro su valor sera la hora y fecha actual del servidor de base de datos por lo que ya no nos tenemos que preocupar en colocar la fecha 
    # db_column > indicar como se tiene que llamar esta columna en la base de datos solamente si queremos cambiar el nombre del atributo
    fechaCreacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    # Forma de indicar que accion debe tomar cuando se elimine el 'padre'
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    # CASCADE > Cuando se elimine una categoria en forma de cascada se eliminaran todos los platos
    # PROTECT > Evita la eliminacion de la categoria si esta tiene platos que dependan de ella, emitira un error ProtectedError
    # RESTRICT > Restinge la eliminacion, es lo mismo que el PROTECT solo que emitira un error de tipo RestrictedError
    # SET_NULL > permite la eliminacion de la categoria y a los platos que dependan de ella les cambiar su valor por NULL
    # SET_DEFAULT > permite la eliminacion de la categoria y les cambiar el valor a un valor por defecto
    # DO_NOTHING > permite la eliminacion PERO no hace nada osea mantiene el mismo numero de categoria en el plato a pesar que este no exista generando un problema de integridad 

    categoria = models.ForeignKey(to=CategoriaModel, on_delete=models.PROTECT, db_column='categoria_id')
    
    class Meta:
        db_table = 'platos'
