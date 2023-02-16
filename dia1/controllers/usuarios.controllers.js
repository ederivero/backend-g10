import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";

const usuarios = [];

export const registroUsuario = async (req, res) => {
  // {'nombre': 'eduardo', 'apellido': 'de rivero', 'correo': 'ederiveroman@gmail.com', 'password':'Welcome123'}
  const data = req.body;
  const passwordHashed = bcrypt.hashSync(data.password, 10);
  console.log(passwordHashed);

  // TODO: reemplazar por base de datos
  usuarios.push({ ...data, password: passwordHashed });

  return res
    .json({
      message: "Usuario creado exitosamente",
    })
    .status(201);
};

export const login = async (req, res) => {
  // { "correo": "ederiveroman@gmail.com", "password": "Welcome123"}
  const data = req.body;

  // TODO : reemplazar por base de datos
  // encontrar el usuario en el arreglo
  const usuarioEncontrado = usuarios.find(
    (usuario) => usuario.correo === data.correo
  );

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
    const token = jwt.sign(payload, "ultramegasupersecreto", {
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
