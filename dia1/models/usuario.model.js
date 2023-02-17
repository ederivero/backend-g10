import mongoose from "mongoose";

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
        console.log(valor);
        return "123";
      },
    },
  },
  // Configuraciones de la coleccion
  {
    timestamps: {
      createdAt: true,
      updatedAt: "actualizado",
    },
  }
);

export const UsuarioModel = mongoose.model("usuarios", usuarioSchema);
