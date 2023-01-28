from django.contrib import admin
from .models import ProductosModel, CategoriasModel, ClientesModel

# Register your models here.

class ShowFields(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'estado')

admin.site.register(ProductosModel, ShowFields)
admin.site.register(CategoriasModel)
admin.site.register(ClientesModel)