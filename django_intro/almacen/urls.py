from django.urls import path
from .views import renderHtml, buscarProducto
from .views import ProductosView

urlpatterns = [
    path('productos', renderHtml),
    path('producto/<int:producto_id>', buscarProducto),
    path('productos/listar', ProductosView.as_view())
]