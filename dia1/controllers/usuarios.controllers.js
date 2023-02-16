import bcrypt from "bcryptjs";

const usuarios = [];

export const registroUsuario = async (req, res) => {
  // {'nombre': 'eduardo', 'apellido': 'de rivero', 'correo': 'ederiveroman@gmail.com', 'password':'Welcome123'}
  const data = req.body;
  const passwordHashed = bcrypt.hashSync(data.password, 10);
  console.log(passwordHashed);
  usuarios.push({ ...data, password: passwordHashed });

  return res
    .json({
      message: "Usuario creado exitosamente",
    })
    .status(201);
};
