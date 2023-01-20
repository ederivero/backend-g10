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

@app.route("/productos/eliminar/<str:producto_id>")
def productosEliminar(producto_id):
    controller = ProductosController()
    return controller.eliminarProducto(producto_id)

if __name__ == '__main__':
    app.run(debug=True)