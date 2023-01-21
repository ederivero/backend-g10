from models.productos_model import ProductosModel
from models.categorias_productos_model import CategoriasProductosModel
from db import db

class ProductosController:

    def crearProducto(self, data):
        try:
            producto = ProductosModel(data['nombre'], data['precio'], data['imagen'])
            db.session.add(producto)
            db.session.commit()

            nuevas_categorias = []
            for categoria in data['categorias']:
                nueva_categoria = CategoriasProductosModel(producto.id, categoria['categoria_id'])
                nuevas_categorias.append(nueva_categoria)
            db.session.add_all(nuevas_categorias)
            db.session.commit()
            return {
                'data': producto.convertirJson()
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def listarProductos(self):
        productos = ProductosModel.query.all()
        response = []
        for producto in productos:
            response.append(producto.convertirJson())
        return {
            'data': response
        }, 200

    def eliminarProducto(self, producto_id):
        try:
            producto = ProductosModel.query.filter_by(id=producto_id).first()
            producto.estado = False
            db.session.commit()
            return {
                'message': 'Producto eliminado correctamente'
            }, 200
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def actualizarProducto(self, producto_id, data):
        try:
            producto = ProductosModel.query.filter_by(id=producto_id).first()
            producto.nombre = data['nombre']
            producto.precio = data['precio']
            db.session.commit()
            return {
                'data': producto.convertirJson()
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def buscarProductos(self, precio):
        try:
            productos = ProductosModel.query.filter_by(precio=precio).all()
            response = []
            for producto in productos:
                response.append(producto.convertirJson())
            return {
                'data': response
            }, 200
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500