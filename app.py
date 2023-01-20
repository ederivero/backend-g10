from flask import Flask, request
from controllers.productos_controller import ProductosController
from flask_migrate import Migrate
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def index():
    return "Mi aplicacion con Flask :D"

@app.route("/productos/lista", methods=['GET'])
def productosListar():
    controller = ProductosController()
    return controller.listarProductos()

@app.route("/productos/crear", methods=['POST'])
def productosCrear():
    controller = ProductosController()
    return controller.crearProducto(request.json)

@app.route("/productos/eliminar/<int:producto_id>", methods=['DELETE'])
def productosEliminar(producto_id):
    controller = ProductosController()
    return controller.eliminarProducto(producto_id)

@app.route("/productos/actualizar/<int:producto_id>", methods=['PUT'])
def productosActualizar(producto_id):
    controller = ProductosController()
    return controller.actualizarProducto(producto_id, request.json)

@app.route("/productos/buscar/<float:precio>", methods=['GET'])
def productosBuscar(precio):
    controller = ProductosController()
    return controller.buscarProductos(precio)

if __name__ == '__main__':
    app.run(debug=True)