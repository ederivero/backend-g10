from rest_framework.generics import ListCreateAPIView
from .models import CategoriaModel, PlatoModel
from .serializers import CategoriaSerializer, PlatoSerializer
from rest_framework.response import Response
from rest_framework.request import Request

# List > Listar (get)
# Create > Crear (post)

class CategoriaApiView(ListCreateAPIView):
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
    serializer_class = PlatoSerializer

    def get(self, request: Request):
        # al colocar ':' indicamos que el tipo de dato que sera esa variable en el caso que no la hemos seteado correctamente
        # request > toda la informacion que viene del cliente
        
        # SELECT * FROM platos WHERE disponibilidad = true;
        resultado = PlatoModel.objects.filter(disponibilidad=True).all()
        print(resultado)
        
        return Response(data= {
            'message': 'Me hizo get'
        })