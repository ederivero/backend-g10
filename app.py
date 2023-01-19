from flask import Flask
from controllers.productos import ProductosController

app = Flask(__name__)

@app.route("/")
def index():
    return "Mi aplicacion con Flask :D"

@app.route("/productos", methods=['GET'])
def productos():
    controller = ProductosController()
    return controller.listarProductos()

if __name__ == '__main__':
    app.run(debug=True)