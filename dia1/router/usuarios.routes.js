import { Router } from "express";
import * as usuarioController from "../controllers/usuarios.controllers.js";

export const usuarioRouter = Router();

usuarioRouter.post("/registro", usuarioController.registroUsuario);
