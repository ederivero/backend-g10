// asi se exporta utilizando ECMAscript
import conexion from '../conector_bd.js'

export const crearCategoria = async (req, res) => {
  const { body } = req
  console.log(body)
  // si es que la creacion es exitosa
  // de manera asincrona

  const respuesta = await conexion.categoria.create({
    data: {
      nombre: body.nombre,
    },
  })

  res.json({
    message: 'Se creo la categoria exitosamente',
    content: respuesta,
  })
}

export const listarCategorias = async (req, res) => {
  // SELECT * FROM categorias;
  const respuesta = await conexion.categoria.findMany()

  res.json({
    content: respuesta,
  })
}

export const buscarCategoriaPorId = async (req, res) => {
  console.log(req.params)
  const { id } = req.params
  const resultado = await conexion.categoria.findFirst({ where: { id: +id } })
  if (!resultado) {
    res.json({
      message: 'Categoria no existe',
    })
  }

  res.json({
    content: resultado,
  })
}
// asi se exporta en commonJs
// module.exports = {
//   crearCategoria,
// }
