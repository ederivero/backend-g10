from camelcase import CamelCase

instancia = CamelCase()

texto = 'hola yo deberia esta camel caseado'

resultado = instancia.hump(texto)

print(resultado)