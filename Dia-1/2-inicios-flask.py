from flask import Flask, request
from flask_cors import CORS


# si el archivo es el archivo principal del proyecto su valor de la variable __name__ sera '__main__' caso contrario sera None (vacio)
app = Flask(__name__)

# ahora configuramos nuestros CORS (Control de acceso de Recursos cruzados)
# origins = '*'
# methods = '*'
CORS(app=app, origins=['http://127.0.0.1:5500'], methods=['GET', 'POST'])

# patron de diseño de software (Singleton)

usuarios = [
    {
        'nombre': 'Eduardo',
        'apellido':'Juarez'
    },
    {
        'nombre': 'Juana',
        'apellido': 'Rodriguez'
    },
    {
        'nombre': 'Roberto',
        'apellido': 'Castillo'
    }
]

# un decorador se usa con el '@' y sirve para poder modificar cierto metodo de una clase sin la necesidad de modificar el funcionamiento natural (es una modificacion parcial) luego de utilizar el decorador se crea una funcion que sera la nueva funcionabilidad de ese metodo
@app.route('/')
def inicio():
    return 'Hola desde mi servidor de Flask'


# ENDPOINT (punt final) declaracion de la finalicion de la URL que indicara que accion se debe de realizar
@app.route('/mostrar-hora', methods=['GET','POST'])
def mostrarHora():
    # CONTROLLER (controlador) > es la funcionabilidad que se realizara dentro de un determinado endpoint
    # request > me dara toda la informacion que viene desde el cliente
    print(request.method)
    if request.method == 'GET':
        return {
            'content': 'Me hiciste GET'
        }
    elif request.method == 'POST':
        return {
            'content': 'Me hiciste POST'
        }
    
    # esta parte del codigo sera inaccesible ya que los metodos para acceder siempre seran GET o POST
    # no se suele retornar strings (cadena de texto) sino que se utiliza diccionarios
    return {
        'content': '22:50:15'
    }


@app.route('/usuarios', methods=['GET','POST'])
def gestionUsuario():
    if request.method == 'GET':
        # devolvemos los usuarios
        return {
            'message': 'Los usuarios son',
            'content': usuarios
        }
    elif request.method == 'POST':
        # agregar un nuevo usuario
        # request.data > mostrara la informacion proveniente del body en formato bytes
        # get_json() > convierte el body entrante en un diccionario desde un JSON
        print(request.get_json())
        data = request.get_json()
        usuarios.append(data)
        return {
            'message': 'Usuario agregado exitosamente'
        }


# debug > cada vez que modifiquemos algun archivo del proyecto y guardamos, se reiniciara el servidor
app.run(debug=True)