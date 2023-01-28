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