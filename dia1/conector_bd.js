import prisma from '@prisma/client'

// asi se exporta de manera por defecto (en el caso que tengamos una sola exportacion en nuestro archivo)
// solamente se puede tener una exportacion por defecto
export default new prisma.PrismaClient({
  log: ['query'],
})

// Esto sirve para poder trabajar con el archivo prueba.js
// export default true

// export const nombre = 'eduardo'

// export const edad = 30
