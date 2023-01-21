from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from db import db

class ProductosModel(db.Model):
    __tablename__ = 'productos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    precio = Column(Float, nullable=False)
    estado = Column(Boolean, default=True)

    categorias_productos = relationship('CategoriasProductosModel')

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def convertirJson(self):
        categorias = []
        for categoria_producto in self.categorias_productos:
            categorias.append(categoria_producto.categoria.convertirJson())

        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'estado': self.estado,
            'categorias': categorias
        }