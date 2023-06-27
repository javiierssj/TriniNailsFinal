from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('venta', views.VentaView,'venta')
router.register('producto', views.ProductoView,'producto')

urlpatterns = [
    path('api/v1/', include(router.urls))
    # Agrega más URL según tus necesidades
]