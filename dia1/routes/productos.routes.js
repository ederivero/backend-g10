import { Router } from 'express'
import * as controller from '../controllers/productos.controller.js'

export const productoRouter = Router()

productoRouter.route('/productos').post(controller.crearProducto)

productoRouter.route('/toggle-producto/:id').post(controller.toggleProducto)
