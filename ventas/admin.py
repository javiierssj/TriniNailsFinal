# Register your models here.
from django.contrib import admin
from .models import Venta, DetalleVenta, Producto, Usuario, Administrador, CarritoCompra

admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(CarritoCompra)
