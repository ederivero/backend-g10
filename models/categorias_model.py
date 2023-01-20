from sqlalchemy import Column, Integer, String
from db import db

class CategoriasModel(db.Model):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def convertirJson(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }