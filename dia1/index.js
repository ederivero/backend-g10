import express from "express";
import { usuarioRouter } from "./router/usuarios.routes.js";
import { calendariosRouter } from "./router/calendarios.routes.js";

const server = express();

server.use(express.json());

server.use(usuarioRouter);
server.use(calendariosRouter);

const puerto = 3000;

server.listen(puerto, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${puerto}`);
});
