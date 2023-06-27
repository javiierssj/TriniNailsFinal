from rest_framework import serializers
from .models import Venta, DetalleVenta, Producto, Usuario, Administrador, CarritoCompra


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = '__all__'


class VentaSerializer(serializers.ModelSerializer):
    detalles_venta = DetalleVentaSerializer(many=True)

    class Meta:
        model = Venta
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class AdministradorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Administrador
        fields = '__all__'

class CarritoCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompra
        fields = '__all__'