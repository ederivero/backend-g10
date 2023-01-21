from models.usuarios_model import UsuariosModel
from werkzeug.security import generate_password_hash, check_password_hash
from db import db


class UsuariosController:
    def __init__(self) -> None:
        self.model = UsuariosModel

    def crearUsuario(self, data):
        try:
            contrasena = self.__encriptarContrasena(data['contrasena'])
            usuario = self.model(data['nombres'], data['correo'], data['imagen'], contrasena)
            db.session.add(usuario)
            db.session.commit()
            return {
                'data': usuario.convertirJson()
            }
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def __encriptarContrasena(self, contrasena):
        return generate_password_hash(contrasena)