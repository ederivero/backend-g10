from db import db
from sqlalchemy import Column, String, Integer, Text


class UsuariosModel(db.Model):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(200), nullable=False)
    correo = Column(String(100), nullable=False)
    imagen = Column(Text, nullable=True)
    contrasena = Column(Text, nullable=False)

    def __init__(self, nombres, correo, imagen, contrasena) -> None:
        self.nombres = nombres
        self.correo = correo
        self.imagen = imagen
        self.contrasena = contrasena

    def __str__(self) -> str:
        return self.nombres

    def convertirJson(self):
        return {
            'id': self.id,
            'nombres': self.nombres,
            'correo': self.correo,
            'imagen': self.imagen,
        }