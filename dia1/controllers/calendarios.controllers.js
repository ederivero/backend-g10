const calendarios = [
  {
    correo: "ederiveroman@gmail.com",
    tareas: [
      {
        titulo: "Ir a la piscina",
        descripcion: "Ir a la piscina municipal",
        hora_inicio: "06:00",
        hora_fin: "08:30",
        dias: ["Lun", "Mie", "Vie"],
      },
    ],
  },
  {
    correo: "juancito@gmail.com",
    tareas: [
      {
        titulo: "Ir al partido de voley",
        descripcion: "Ir al club del ingeniero",
        hora_inicio: "21:00",
        hora_fin: "22:30",
        dias: ["Mar", "Vie"],
      },
    ],
  },
];

export const devolverCalendarios = async (req, res) => {
  console.log(req.user);
  return res.json({
    message: "Llegaste al final!",
  });
};
