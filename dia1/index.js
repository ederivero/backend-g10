const express = require("express");
const { PrismaClient } = require("@prisma/client");

const prisma = new PrismaClient();

// se va a copiar toda la funcionabilidad de la libreria express en la variable servidor
const servidor = express();

// que ahora mi servidor podra convertir la informacion entrante para los JSON
// middleware para convertir la informacion entrante a un formato legible
servidor.use(express.json());

// servidor.use(express.urlencoded())

servidor.get("/", (req, res) => {
  // req > es la informacion que me envia el cliente
  // res > es la informacion que voy a devolver al cliente
  res.json({
    message: "Bienvenido a mi API",
  });
});

servidor.post("/productos", (req, res) => {
  console.log(req.body);

  res.json({
    message: "Producto creado exitosamente",
  });
});

servidor.listen(5000, () => {
  console.log("Servidor corriendo exitosamente en el puerto 5000");
});
