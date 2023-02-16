import express from "express";
import { usuarioRouter } from "./router/usuarios.routes.js";

const server = express();

server.use(express.json());

server.use(usuarioRouter);

const puerto = 3000;

server.listen(puerto, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${puerto}`);
});
