from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.categorias_model import Categoria

class CategoriaDto(SQLAlchemyAutoSchema):
    class Meta:
        # sirve para pasarle los metadatos a la clase que estamos herendando, es una clase exclusiva de Python 
        # metadatos son informacion que necesita la clase que estamos heredando como atributos para que pueda funcionar correctamente
        # Sirve para indicar mediante que modelo se tiene que guiar para hacer el mapeo de la informacion
        model = Categoria

