def saludar(nombre):
    print('Hola {}'.format(nombre))

def saludar_varios(nombre1, nombre2):
    print('Hola {}, {}'.format(nombre1, nombre2))

def saludar_ilimitado(*args):
    # args > arguments
    # args se almacenan en una tupla
    print('Hola')
    for arg in args:
        print(arg)

def definir_personas_ilimitadas(**kwargs):
    # kwargs > keyword argument
    # kwargs como vienen con parametro y valor estos se almacenan en un diccionario
    print(kwargs)

saludar('Eduardo')

saludar_varios('Julio', 'Arnold')

saludar_ilimitado('Elvia', 'Jack', 'Stephani', 'Jhostym')
saludar_ilimitado('Eduardo', 'Paolo')


saludar_varios(nombre2='Juanita', nombre1='Pepito')

definir_personas_ilimitadas(nombre='eduardo', apellido='de rivero', correo='ederiveroman@gmail.com')

definir_personas_ilimitadas(color='mostaza', mes='agosto', soltero=False)


def sumar(num1, num2, num3):
    print(num1+ num2+ num3)

sumar(1,5,9)

numeros = {
    'num1': 10,
    'num2': 20,
    'num3': 50
}

# cuando nosotros tenemos una funcion que recibe ciertos parametros y a su vez tenemos un diccionario con esos mismos parametros que recibe entonces en podemos pasarle el diccionario destructurado (utilizando los dos asteriscos **)
sumar(**numeros)