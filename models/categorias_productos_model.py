from db import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class CategoriasProductosModel(db.Model):
    __tablename__ = 'categorias_productos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    producto_id = Column(Integer, ForeignKey('productos.id'))

    categoria = relationship('CategoriasModel')

    def __init__(self, producto_id, categoria_id) -> None:
        self.producto_id = producto_id
        self.categoria_id = categoria_id