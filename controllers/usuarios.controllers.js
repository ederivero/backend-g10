import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import { UsuarioModel } from "../models/usuario.model.js";
import { enviarCorreo } from "../utils/correo.js";

export const registroUsuario = async (req, res) => {
  // {'nombre': 'eduardo', 'apellido': 'de rivero', 'correo': 'ederiveroman@gmail.com', 'password':'Welcome123'}
  const data = req.body;
  try {
    const nuevoUsuario = await UsuarioModel.create(data);

    await enviarCorreo(
      nuevoUsuario.correo,
      "Hola por favor, haz click en el siguiente enlace para verificar tu cuenta"
    );

    return res
      .json({
        message: "Usuario creado exitosamente",
        content: nuevoUsuario.toJSON(),
      })
      .status(201);
  } catch (error) {
    if (error.name === "MongoServerError" && error.code === 11000) {
      return res
        .json({
          message: "El usuario ya existe",
        })
        .status(400);
    }

    return res
      .json({
        message: "Error al crear el usuario, intentelo nuevamente",
      })
      .status(400);
  }
};

export const login = async (req, res) => {
  // { "correo": "ederiveroman@gmail.com", "password": "Welcome123"}
  const data = req.body;

  const usuarioEncontrado = await UsuarioModel.findOne({ correo: data.correo });

  if (!usuarioEncontrado) {
    return res.status(404).json({
      message: "Usuario no existe",
    });
  }

  const resultado = bcrypt.compareSync(
    data.password,
    usuarioEncontrado.password
  );

  if (resultado) {
    // es la informacion adicional que usara la token
    const payload = {
      correo: usuarioEncontrado.correo,
      mensaje: "hola",
    };
    // aca creo la token
    const token = jwt.sign(payload, process.env.JWT_SECRET_KEY, {
      expiresIn: "1h",
    });

    return res.json({
      message: "Bienvenido",
      content: token,
    });
  } else {
    return res.status(403).json({
      message: "Usuario no existe",
    });
  }
};
