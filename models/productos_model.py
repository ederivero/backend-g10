from app import db
from sqlalchemy import Column, Integer, String, Float

class ProductosModel(db.Model):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(45))
    precio = Column(Float)