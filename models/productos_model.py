from sqlalchemy import Column, Integer, String, Float
from db import db

class ProductosModel(db.Model):
    __tablename__ = 'productos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45))
    precio = Column(Float)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio