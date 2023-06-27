from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Venta, Producto
from rest_framework import viewsets
from .serializers import VentaSerializer, DetalleVentaSerializer, ProductoSerializer, UsuarioSerializer, AdministradorSerializer, CarritoCompraSerializer

class VentaView(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()

class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()   
