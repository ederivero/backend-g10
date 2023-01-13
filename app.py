from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_restful import Api

from models.categorias_model import Categoria
from models.productos_model import Producto
from models.categorias_productos_model import CategoriaProducto

from controllers.categoria_controller import CategoriasController


# aca utilizaremos el archivo .env para agregarlo a las variables de entorno
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= environ.get('DATABASE_URL')

# inicializamos nuestra clase Api
api = Api(app)

# inicializar la aplicacion de SQLAlchemy con nuestra aplicacion de flask
conexion.init_app(app)

# Inicializamos la clase Migrate pasandole nuestra aplicacion de Flask y nuestra conexion a SQLAlchemy
Migrate(app,conexion)

# Asi utilizariamos la creacion de las tablas sin utilizar migraciones
# este controlador se ejecutara antes del primer request de nuestro servidor
@app.before_first_request
def inicializadora():
    # realizar la creacion de todos los modelos de nuestro proyecto como tablas en la base de datos
    # conexion.create_all()
    pass

api.add_resource(CategoriasController, '/categorias')


if __name__ == '__main__':
    app.run(debug=True)