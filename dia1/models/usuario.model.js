import mongoose from "mongoose";
import bcrypt from "bcryptjs";

// Datatypes de mongoose > https://mongoosejs.com/docs/schematypes.html
// Configuracion de las columnas > https://mongoosejs.com/docs/schematypes.html#schematype-options
// NOTA: todas estas configuracion SOLAMENTE funcionaran en mongoose, es decir si agregamos data directamente en mongo ninguna de estas tendra validez

const usuarioSchema = new mongoose.Schema(
  {
    nombre: {
      type: mongoose.Schema.Types.String,
      required: true,
      maxLength: 50,
    },

    apellido: {
      type: mongoose.Schema.Types.String,
      maxLength: 50,
    },

    correo: {
      type: mongoose.Schema.Types.String,
      required: true,
      index: true,
      unique: true,
    },

    password: {
      type: mongoose.Schema.Types.String,
      required: true,
      set: (valor) => {
        // servira para cuando queramos modificar o establer el valor de esta propiedad
        const passwordHashed = bcrypt.hashSync(valor, 10);
        console.log(valor);
        return passwordHashed;
      },
    },
  },
  // Configuraciones de la coleccion
  {
    timestamps: {
      createdAt: true, // se registre un nuevo usuario tomara la hora de la base de datos
      updatedAt: "actualizado", // se actualice alguna informacion de un usuario cambiara su hora y fecha a la hora actual de la base de datos
    },
  }
);

export const UsuarioModel = mongoose.model("usuarios", usuarioSchema);
