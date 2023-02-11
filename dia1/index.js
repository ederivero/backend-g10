// asi se importa utilizando ECMAscript
import express from 'express'

import {
  crearCategoria,
  listarCategorias,
  buscarCategoriaPorId,
  actualizarCategoria,
  eliminarCategoria,
} from './controllers/categorias.controller.js'
import { productoRouter } from './routes/productos.routes.js'

// asi se importa utilizanco commonJs
// const express = require('express')
// const { PrismaClient } = require('@prisma/client')
// const { crearCategoria } = require('./controllers/categorias.controller')

// se va a copiar toda la funcionabilidad de la libreria express en la variable servidor
const servidor = express()

// que ahora mi servidor podra convertir la informacion entrante para los JSON
// middleware para convertir la informacion entrante a un formato legible
servidor.use(express.json())

// servidor.use(express.urlencoded())

servidor.get('/', (req, res) => {
  // req > es la informacion que me envia el cliente
  // res > es la informacion que voy a devolver al cliente
  res.json({
    message: 'Bienvenido a mi API',
  })
})

// conjunto de rutas
servidor.use(productoRouter)

servidor.route('/categorias').post(crearCategoria).get(listarCategorias)
servidor.route('/categoria/:id').get(buscarCategoriaPorId).put(actualizarCategoria).delete(eliminarCategoria)

servidor.post('/productos', (req, res) => {
  console.log(req.body)

  res.json({
    message: 'Producto creado exitosamente',
  })
})

servidor.listen(8080, () => {
  console.log('Servidor corriendo exitosamente en el puerto 8080')
})
