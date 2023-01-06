from flask import Flask, request
from flask_mysqldb import MySQL
# Devuelve todas las variables de entorno de este dispositivo
from os import environ

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# cuando tenemos un diccionario poder OBTENER el valor de una de sus llaves con el metodo .get('LLAVE'), SOLO es para obtener, no para asignar. Y si que al obtener no hay valor entonces colocara None (vacio)
# ESTO NO SE PUEDE HACER:
# environ.get('MYSQL_HOST') = 'hola'
# environ['MYSQL_HOST'] = 'hola'
app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(environ.get('MYSQL_PORT'))

# Cuando a una variable se le asigna una clase se llama INSTANCIA
# inicializamos la conexion seteando todos los parametros de nuestra bd, PERO AUN NO NOS HEMOS CONECTADO
mysql = MySQL(app)

@app.route('/productos', methods=['GET', 'POST'])
def gestion_productos():
    if request.method == 'GET':
        # crea una conexion a la base de datos mediante un cursor
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall() # LIMIT infinito
        # cursor.fetchone() # LIMIT 1
        print(productos)
        # cerra nuestra conexion
        cursor.close()
        return {
            'message': 'Los productos son'
        }
    elif request.method == 'POST':
        return {
            'message': 'Producto creado exitosamente'
        }



# load_dotenv > cargamos todas las variables definidas en el archivo .env como si fueran variables de entorno
app.run(debug=True, load_dotenv=True)