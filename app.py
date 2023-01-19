from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.productos_controller import ProductosController

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

@app.route("/")
def index():
    return "Mi aplicacion con Flask :D"

@app.route("/productos", methods=['GET'])
def productos():
    controller = ProductosController()
    return controller.listarProductos()

if __name__ == '__main__':
    app.run(debug=True)