import express from "express";
import { usuarioRouter } from "./router/usuarios.routes.js";
import { calendariosRouter } from "./router/calendarios.routes.js";
import mongoose from "mongoose";

const server = express();

server.use(express.json());

server.use(usuarioRouter);
server.use(calendariosRouter);

const puerto = 3000;

server.listen(puerto, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${puerto}`);
  mongoose.set("strictQuery", true);
  mongoose
    .connect("mongodb://127.0.0.1:27017/agendas")
    .then((valor) => {
      console.log("Se conecto a la base de datos exitosamente");
    })
    .catch((error) => {
      console.log("Error al conectarse a la base");
    });
});
