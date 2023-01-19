from flask import Flask
from controllers.productos_controller import ProductosController
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

db.init_app(app)

@app.route("/")
def index():
    return "Mi aplicacion con Flask :D"

@app.route("/productos", methods=['GET'])
def productos():
    controller = ProductosController()
    return controller.listarProductos()

if __name__ == '__main__':
    app.run(debug=True)