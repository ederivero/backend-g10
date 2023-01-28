from rest_framework import serializers
from .models import ProductosModel, CategoriasModel, ClientesModel, OrdenesModel


class ProductosSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(read_only=True)
    class Meta:
        model = ProductosModel
        # fields = ['nombre', 'precio']
        fields = '__all__'
        # exclude = ['estado']

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasModel
        fields = '__all__'
    
    def delete(self):
        self.instance.estado = False
        self.instance.save()
        return self.instance

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientesModel
        fields = '__all__'

class OrdenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenesModel
        fields = '__all__'