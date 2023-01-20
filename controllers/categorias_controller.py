from models.categorias_model import CategoriasModel
from db import db

class CategoriasController:
    def __init__(self) -> None:
        self.model = CategoriasModel

    def crearCategoria(self, data):
        try:
            categoria = self.model(data['nombre'])
            db.session.add(categoria)
            db.session.commit()
            return {
                'data': categoria.convertirJson()
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def listarCategorias(self):
        try:
            categorias = self.model.query.all()
            # categorias = self.model.query.filter_by(estado=True).all()
            response = []
            for categoria in categorias:
                response.append(categoria.convertirJson())
            return {
                'data': response
            }, 200
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def actualizarCategoria(self, categoria_id, data):
        try:
            categoria = self.model.query.get(categoria_id)
            categoria.nombre = data['nombre']
            db.session.commit()
            return {
                'data': categoria.convertirJson()
            }
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def eliminarCategoria(self, categoria_id):
        try:
            categoria = self.model.query.get(categoria_id)
            categoria.estado = False
            db.session.commit()
            return {
                'data': categoria.convertirJson()
            }
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500