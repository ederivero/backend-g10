from models.productos_model import ProductosModel
from db import db

class ProductosController:

    def crearProducto(self, data):
        try:
            producto = ProductosModel(data['nombre'], data['precio'])
            db.session.add(producto)
            db.session.commit()
            return {
                'data': producto.json()
            }
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
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

    def eliminarProducto(self, producto_id):
        try:
            producto = ProductosModel.query.get(id=producto_id)
            print(producto)
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }