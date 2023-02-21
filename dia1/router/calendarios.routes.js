import { Router } from "express";
import * as calendariosController from "../controllers/calendarios.controllers.js";

export const calendariosRouter = Router();

// Primera forma se usa cuando las rutas y middleware son diferentes

// calendariosRouter.get(
//   "/calendarios",
//   validarToken,
//   calendariosController.devolverCalendarios
// );

// calendariosRouter.post(
//   "/calendarios",
//   validarToken,
//   calendariosController.crearCalendario
// );

// En todos los metodos del calendario de la misma ruta se que voy a utilizar un middleware en comun
calendariosRouter
  .route("/calendarios")
  .post(calendariosController.crearCalendario)
  .get(calendariosController.devolverCalendarios);

// En la cual tambien se repetiria el mismo middleware y se tiene que configurar por cada metodo HTTP de manera independiente
// calendariosRouter
//   .route("/calendarios")
//   .post(validarToken, calendariosController.crearCalendario)
//   .get(validarToken, calendariosController.devolverCalendarios);

calendariosRouter
  .route("/calendario/:id")
  .put(calendariosController.actualizarCalendario)
  .delete(calendariosController.eliminarCalendario);
