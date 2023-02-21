import { CalendarioModel } from "../models/calendario.model.js";
import { UsuarioModel } from "../models/usuario.model.js";

export const devolverCalendarios = async (req, res) => {
  console.log(req.user);
  // buscar todos los calendarios que tengan ese id , recordemos que req.user.calendarios es un arreglo de id's por lo que lo tenemos que iterar y buscar cada  calendario
  const resultado_de_promesas = req.user.calendarios.map(
    async (calendarioId) => {
      const calendarioEncontrado = await CalendarioModel.findById(calendarioId);
      return calendarioEncontrado;
    }
  );

  const resultado = await Promise.all(resultado_de_promesas);

  console.log(resultado);

  return res.json({
    content: resultado,
  });
};

export const crearCalendario = async (req, res) => {
  const data = req.body;
  const idUsuario = req.user._id;
  // { "titulo": "Ir a marchar", "descripcion": "Ir a izar el pabellon nacional", "hora_inicio":"10:00", "hora_fin":"12:00", "dias": ["LUN", "MIE", "DOM"]}

  // Una vez que cree el nuevo calendario
  const calendario_creado = await CalendarioModel.create({
    ...data,
    usuario: idUsuario,
  });

  // Ahora registro en el usuario el calendario creado
  const usuario_encontrado = await UsuarioModel.findById(idUsuario);
  usuario_encontrado.calendarios.push(calendario_creado._id);
  // ahora guardamos la informacion modificada del usuario en la base de datos
  await usuario_encontrado.save();

  return res.json({
    message: "Calendario agregado exitosamente",
    content: calendario_creado,
  });
};

export const actualizarCalendario = async (req, res) => {
  const { id } = req.params;
  const data = req.body;
  console.log(id);
  try {
    const calendario = await CalendarioModel.findOne({
      _id: id,
      usuario: req.user._id,
    });

    if (!calendario) {
      return res.status(404).json({
        message: "Calendario no existe",
      });
    }
    // diferencia entre updateOne y findOneAndUpdate es que el segundo lo encontrara y lo devolvera mientras que el primero solamente actualizara y devolvera la informacion de la actualizacion
    const calendario_actualizado = await CalendarioModel.findOneAndUpdate(
      { _id: calendario._id },
      data,
      { new: true } // para indicar que queremos que nos devuelva el registro ya actualizado
    );

    return res.json({
      message: "Calendario actualizado exitosamente",
      content: calendario_actualizado,
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al actualizar el calendario",
    });
  }
};

export const eliminarCalendario = async (req, res) => {
  const { id } = req.params;

  try {
    const resultado = await CalendarioModel.deleteOne({
      _id: id,
      usuario: req.user._id,
    });

    if (resultado.deletedCount === 0) {
      return res.json({
        message: "Calendario no existe",
      });
    } else {
      return res.json({
        message: "Calendario eliminado exitosamente",
      });
    }
  } catch (error) {
    return res.status(400).json({
      message: "Error al eliminar el calendario",
    });
  }
};
