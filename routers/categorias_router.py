from app import app
from controllers.categorias_controller import CategoriasController
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route("/categorias/crear", methods=['POST'])
def categoriasCrear():
    controller = CategoriasController()
    return controller.crearCategoria(request.json)

@app.route("/categorias/actualizar/<int:categoria_id>", methods=['PUT'])
def categoriasActualizar(categoria_id):
    controller = CategoriasController()
    return controller.actualizarCategoria(categoria_id, request.json)

@app.route("/categorias/eliminar/<int:categoria_id>", methods=['DELETE'])
def categoriasEliminar(categoria_id):
    controller = CategoriasController()
    return controller.eliminarCategoria(categoria_id)

@app.route("/categorias/listar", methods=['GET'])
@jwt_required()
def categoriasListar():
    user_id = get_jwt_identity()
    controller = CategoriasController()
    return controller.listarCategorias(user_id)

@app.route("/categorias/importar", methods=['GET'])
def categoriasImportar():
    controller = CategoriasController()
    return controller.importarExcel()