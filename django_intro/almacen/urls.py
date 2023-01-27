from django.urls import path
from .views import renderHtml, buscarProducto
from .views import ProductosView, CategoriasView, ActualizarCategoriasView

urlpatterns = [
    path('productos', renderHtml),
    path('producto/<int:producto_id>', buscarProducto),
    path('productos/listar', ProductosView.as_view()),
    path('categorias/listar/', CategoriasView.as_view()),
    path('categorias/actualizar/<int:categoria_id>', ActualizarCategoriasView.as_view())
]