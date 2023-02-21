import { CalendarioModel } from "../models/calendario.model.js";

export const devolverCalendarios = async (req, res) => {
  console.log(req.user);

  return res.json({
    content: req.user.calendarios,
  });
};
