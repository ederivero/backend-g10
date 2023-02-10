from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from .models import CategoriaModel, PlatoModel, UsuarioModel
from .serializers import CategoriaSerializer, CrearPlatoSerializer, CategoriaConPlatosSerializer, MostrarPlatoSerializer, RegistroUsuarioSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .permissions import SoloAdministradores, SoloMozos, SoloTrabajador
# List > Listar (get)
# Create > Crear (post)

class CategoriaApiView(ListCreateAPIView):
    # secuencia de permisos > el primer permiso se debe de cumplir para continuar con el segundo permiso y asi sucesivamente, si alguno falla (retorna False) entonces todo termina
    permission_classes = [IsAuthenticated, SoloAdministradores]
    # al utilizar una vista generica que ya no es necesario definir el comportamiento para cuando sea get o post
    # queryset > el comando que utilizara para llamar a la informacion de nuestra base de datos
    # SELECT * FROM categoria;
    queryset = CategoriaModel.objects.all()
    # serializer_class > se define una clase que se encargara de convertir y transformar la informacion que viene desde el cliente y la informacion que enviamos hacia el cliente en dato legibles

    serializer_class = CategoriaSerializer
    # ya no es necesario definir los metodos 'get' y 'post'
    # def get(self):
    #     pass

    # def post(self):
    #     pass

class PlatoApiView(ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    # serializer_class > cuando nosotros modificamos la funcionabilidad de los metodos ya no es necesario definir los atributos obligatorios (y queryset)

    def get(self, request: Request):
        # al colocar ':' indicamos que el tipo de dato que sera esa variable en el caso que no la hemos seteado correctamente
        # request > toda la informacion que viene del cliente
        
        # SELECT * FROM platos WHERE disponibilidad = true;
        resultado = PlatoModel.objects.filter(disponibilidad=True).all()
        print(resultado)
        # aca llamamos al serializer y le pasamos la informacion proveniente de la bd y con el parametro many True indicamos que le estamos pasando un arreglo de instancias
        serializador = MostrarPlatoSerializer(instance=resultado, many=True)
        print(serializador.data)

        return Response(data= {
            'content': serializador.data
        })
    

    def post(self, request:Request):
        body = request.data
        # cuando queremos verificar si la informacion entrante es valida entonces utilizamos el parametro data en vez del parametro instance
        serializador = CrearPlatoSerializer(data=body)

        # es el encargado de validar si la data es correcta y cumple con todos los requisitos
        valida = serializador.is_valid()

        # SELECT * FROM platos WHERE nombre = '...' LIMIT 1;
        platoExistente = PlatoModel.objects.filter(nombre = body.get('nombre')).first()

        if platoExistente : 
            return Response(data={
                'message': 'El plato con nombre {} ya existe'.format(platoExistente.nombre)
            })

        if valida == False:
            return Response(data={
                'message': 'La informacion es invalida',
                # error > mostrar los errores SOLAMENTE cuando la data no sea valida
                'content': serializador.errors

            })


        # si la data pasada al serializador es una data valida entonces esta informacion se guardara en el atributo validated_data que es un diccionario, el validated_data solamente estara disponible cuando mandemos a la validacion, si no se hace la validacion el validated_data sera vacio
        # platoExistente = PlatoModel.objects.filter(nombre = serializador.validated_data.get('nombre')).first()

        # if platoExistente : 
        #     return Response(data={
        #         'message': 'El plato con nombre {} ya existe'.format(platoExistente.nombre)
        #     })
        
        print(serializador.validated_data)
        # asi guardamos la informacion en la base de datos utilizando el serializador
        nuevoPlato = serializador.save()
        print(nuevoPlato)

        serializar = MostrarPlatoSerializer(instance=nuevoPlato)
        return Response(data={
            'message': 'Plato creado exitosamente',
            # data > es la informacion convertida a un diccionario para que pueda ser entendida por el cliente
            'content': serializar.data
        })


class PlatoDestroyApiView(DestroyAPIView):
    # queryset = PlatoModel.objects.all()
    # serializer_class = PlatoSerializer
    permission_classes = [IsAuthenticated, SoloTrabajador]
    def delete(self, request: Request, pk: int):
        print(pk)
        platoEncontrado = PlatoModel.objects.filter(id = pk, disponibilidad = True).first()

        if platoEncontrado is None:
            return Response(data={
                'message': 'El plato no existe'
            })
        
        # Le cambiamos la disponibilidad
        platoEncontrado.disponibilidad = False
        
        # guardamos los cambios en la bd
        platoEncontrado.save()

        return Response(data={
            'message': 'Plato eliminado exitosamente'
        })

class ListarCategoriaApiView(ListAPIView):
    def get(self, request:Request, pk : int):
        # SELECT * FROM CATEGORIAS WHERE ID = ... LIMIT 1;
        categoriaEncontrada = CategoriaModel.objects.filter(id= pk).first()
        print(categoriaEncontrada)

        if categoriaEncontrada is None:
            return Response(data={
                'message': 'Categoria no existe'
            })
        # dir(instancia) > nos muestra todos los atributos y metodos de la clase
        # print(dir(categoriaEncontrada))
        
        # SELECT * FROM platos WHERE categoria_id = ... AND id = 10;
        print(categoriaEncontrada.platos.filter(id=10).all())
        plato = categoriaEncontrada.platos.all()[0] # estamos accediendo al primer plato de esta categoria
        print(plato.nombre)
        print(plato.id)
        print(plato.precio)
        print(plato.fechaCreacion)

        serializador = CategoriaConPlatosSerializer(instance=categoriaEncontrada)


        return Response(data={
            'content': serializador.data
        })

class RegistroUsuarioApiView(CreateAPIView):
    def post(self, request: Request):
        serializador = RegistroUsuarioSerializer(data = request.data)
        validacion = serializador.is_valid()

        if validacion is False:
            return Response(data={
                'message': 'error al crear el usuario',
                'content': serializador.errors
            }, status=400)
        
        # inicializo el nuevo usuario con la informacion validada
        nuevoUsuario = UsuarioModel(**serializador.validated_data)
        # ahora genero el hash de la contraseña
        nuevoUsuario.set_password(serializador.validated_data.get('password'))
        # guardo el usuario en la base de datos
        nuevoUsuario.save()

        return Response(data={
            'message': 'Usuario creado exitosamente'
        }, status=201)