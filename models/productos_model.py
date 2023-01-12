from configuracion import conexion
from sqlalchemy import Column, types

class Producto(conexion.Model):
    id = Column(type_ = types.Integer, autoincrement = True, primary_key = True)
    nombre = Column(type_ = types.String(50), unique = True, nullable = False)
    precio = Column(type_ = types.Float())
    disponible = Column(type_ = types.Boolean, default = True)

    __tablename__ = 'productos'