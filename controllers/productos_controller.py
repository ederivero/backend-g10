from models.productos_model import ProductosModel
from db import db

class ProductosController:

    def create(self):
        producto = ProductosModel('Zapatillas Nike', 200.50)
        db.session.add(producto)
        db.session.commit()
        return {
            'data': 'Texto cualquiera'
        }

    def listarProductos(self):
        productos = ProductosModel.query.all()
        response = []
        for producto in productos:
            response.append({
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio
            })
        return {
            'data': response
        }