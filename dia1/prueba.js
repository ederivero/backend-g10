import variable from './conector_bd.js'
import { nombre, edad } from './conector_bd.js'

// importacion sin destructuracion sera la relacionada  la exportacion por defecto
console.log('variable', variable)
// importacion con desctructuracion sera la exportacion que no es por defecto
console.log('nombre', nombre)
console.log('edad', edad)
