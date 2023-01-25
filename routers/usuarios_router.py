from app import app
from controllers.usuarios_controller import UsuariosController
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request


@app.route("/auth/registrar", methods=['POST'])
def usuariosRegistrar():
    controllador = UsuariosController()
    return controllador.crearUsuario(request.json)

@app.route("/auth/autenticar", methods=['POST'])
def usuariosAutenticar():
    controller = UsuariosController()
    return controller.iniciarSesion(request.json)

@app.route("/auth/refresh", methods=['GET'])
@jwt_required(refresh=True)
def usuariosRefresh():
    identity = get_jwt_identity()
    controller = UsuariosController()
    return controller.refreshSesion(identity)