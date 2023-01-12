from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv

from models.categorias_model import Categoria

# aca utilizaremos el archivo .env para agregarlo a las variables de entorno
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= environ.get('DATABASE_URL')

# inicializar la aplicacion de SQLAlchemy con nuestra aplicacion de flask
conexion.init_app(app)

# este controlador se ejecutara antes del primer request de nuestro servidor
@app.before_first_request
def inicializadora():
    # realizar la creacion de todos los modelos de nuestro proyecto como tablas en la base de datos
    conexion.create_all()

if __name__ == '__main__':
    app.run(debug=True)