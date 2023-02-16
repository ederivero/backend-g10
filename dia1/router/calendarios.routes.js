import { Router } from "express";
import * as calendariosController from "../controllers/calendarios.controllers.js";
import { validarToken } from "../utils/validador.js";

export const calendariosRouter = Router();

calendariosRouter.get(
  "/calendarios",
  validarToken,
  calendariosController.devolverCalendarios
);
