import jwt from "jsonwebtoken";

export const validarToken = (req, res, next) => {
  // primero valido si me estan pasando en las cabeceras, la cabecera de autorizacion
  if (!req.headers.authorization) {
    return res.status(401).json({
      message: "Se necesita una token para realizar esta peticion",
    });
  }
  // Bearer xxxxx.xxxxx.xxxx
  // ['Bearer', 'xxxxx.xxxxx.xxxx']
  const token = req.headers.authorization.split(" ")[1];

  if (!token) {
    return res.status(401).json({
      message:
        "Formato de token invalido, debe ser en el formato Bearer <tu_token>",
    });
  }

  try {
    // si la token es valida entonces me retorna el payload caso contrario me emitira un error
    const payload = jwt.verify(token, "ultramegasupersecreto");
    console.log(payload);

    // si todo esta bien le indicaremos que pase al siguiente controlador
    next();
  } catch (error) {
    return res.status(401).json({
      message: "Erro en la token",
      content: error.message,
    });
  }
};
