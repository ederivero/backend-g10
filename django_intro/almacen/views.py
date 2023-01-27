from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductosModel, CategoriasModel
from .serializers import ProductosSerializer, CategoriasSerializer
from rest_framework import generics, status
from rest_framework.response import Response

def renderHtml(request):
    return HttpResponse("<button>Dame click</button>")

def buscarProducto(request, producto_id):
    producto = ProductosModel.objects.filter(id=producto_id).first()
    return HttpResponse(f'El producto encontrado se llama {producto.nombre} y el precio es: {producto.precio}')

class ProductosView(generics.ListCreateAPIView):
    queryset = ProductosModel.objects.all()
    serializer_class = ProductosSerializer

class CategoriasView(generics.GenericAPIView):
    serializer_class = CategoriasSerializer
    queryset = CategoriasModel.objects.all()

    def get(self, request):
        try:
            record = self.get_queryset()
            serializer = self.get_serializer(record, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data = {
                    'message': 'Internal server error',
                    'error': str(e)
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            categoria = self.get_serializer(data=request.data)
            if categoria.is_valid():
                categoria.save()
                return Response(categoria.data, status=status.HTTP_201_CREATED)

            error = 'Faltan campos'
            for campo in categoria.errors:
                error = error + ' ' + campo + ', '
            return Response({
                'message': error
            })
        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ActualizarCategoriasView(generics.GenericAPIView):
    queryset = CategoriasModel.objects.all()
    serializer_class = CategoriasSerializer

    def get(self, request, categoria_id):
        try:
            record = self.get_queryset().get(id=categoria_id)
            serializer = self.get_serializer(record)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, categoria_id):
        try:
            categoria = self.get_queryset().get(id=categoria_id)
            serializer = self.get_serializer(categoria, data=request.data)
            if serializer.is_valid():
                categoria_actualizada = serializer.update(categoria, serializer.validated_data)
                nuevo_serializador = self.get_serializer(categoria_actualizada)
                return Response(nuevo_serializador.data, status=status.HTTP_201_CREATED)

            error = 'Faltan campos'
            for campo in categoria.errors:
                error = error + ' ' + campo + ', '
            return Response({
                'message': error
            })
        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def delete(self, request, categoria_id):
        try:
            categoria = self.get_queryset().get(id=categoria_id)
            serializador = self.get_serializer(categoria)
            serializador.delete()
            return Response({
                'message': 'Categoria eliminada correctamente'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)