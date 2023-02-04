from django.urls import path
from .views import CategoriaApiView, PlatoApiView, PlatoDestroyApiView, ListarCategoriaApiView


urlpatterns = [
    # cuando se acceda a la ruta /categorias/ se mandara a llamar a la funcionabilidad de nuestro CategoriaApiView
    path('categorias/', CategoriaApiView.as_view()),
    path('platos/', PlatoApiView.as_view()),
    path('plato/<int:pk>', PlatoDestroyApiView.as_view()),
    path('categoria/<int:pk>', ListarCategoriaApiView.as_view()),
]