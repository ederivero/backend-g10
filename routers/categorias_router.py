from app import app
from controllers.categorias_controller import CategoriasController
from flask import request


@app.route("/categorias/crear", methods=['POST'])
def categoriasCrear():
    controller = CategoriasController()
    return controller.crearCategoria(request.json)

@app.route("/categorias/eliminar/<int:categoria_id>")
def categoriasEliminar():
    controller = CategoriasController()
    return controller.eliminarCategoria()


@app.route("/categorias/listar", methods=['GET'])
def categoriasListar():
    controller = CategoriasController()
    return controller.listarCategorias()