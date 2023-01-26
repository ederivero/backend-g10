from rest_framework import serializers
from .models import ProductosModel


class ProductosSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(read_only=True)
    class Meta:
        model = ProductosModel
        # fields = ['nombre', 'precio']
        fields = '__all__'
        # exclude = ['estado']
