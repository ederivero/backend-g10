## Crear el entorno virtual

```
python -m venv venv
```

## Activar el entorno virtual

```
venv\Scripts\activate
source venv/Scripts/activate
source venv/bin/activate
deactivate
```

## Instalar Django

```
pip install Django
pip freeze > requirements.txt
```

## Crear nuestro proyecto

```
django-admin startproject django_intro
```

## Correr el servicio

```
cd django_intro
python manage.py runserver
```

## Migrar los modelos

```
python manage.py migrate
```

## Crear un superusuario

```
python manage.py createsuperuser
```

## Crear una app

```
python manage.py startapp almacen
```

## Registramos nuestra app en INSTALLED_APPS `settings.py`

```python
INSTALLED_APPS = [
    ...,
    'almacen'
]
```

## Crear nuestro nuevo model y migrar

```
python manage.py makemigrations
python manage.py migrate
```

## Instalar Django Rest Framework

```
pip install djangorestframework
```

## Agregar DRF a INSTALLLED_APPS

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Documentar nuestra API con Swagger y Redoc

```
pip install drf-yasg
```

## Configurar `drf-yasg`

```python
INSTALLED_APPS = [
   ...
   'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
   'drf_yasg',
   ...
]
```

En `urls.py`

```python
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Ecommerce API",
      default_version='v1',
      description="Ecommerce para una tienda de zapatillas",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    ...,
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ...
]
```