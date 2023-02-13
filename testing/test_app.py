import pytest

from flask import Flask
from app import app
from flask_migrate import upgrade


@pytest.fixture()
def client():
    client = app.test_client()
    with app.app_context():
        upgrade()
    yield client


class Test:
    def test_categoria_get(self, client: Flask):
        """Listar todas las categorias"""
        request = client.get('/categorias')
        assert request.json == {'content': []}

    def test_categoria_post(self, client: Flask):
        """Crear una categoria"""
        request = client.post('/categorias', json={
            'nombre': 'Cat1'
        })
        assert request.json == {'message': 'Categoria creada exitosamente'}

    def test_categoria_get_2(self, client):
        """Categoria que no existe"""
        request = client.get('/categoria/100')
        assert request.status_code == 400
        assert request.json == {'message': 'La categoria no existe'}

    def test_categoria(self, client):
        """Categoria existe"""
        request = client.get('/categoria/1')
        assert request.status_code == 200
        assert 'content' in request.json
        assert 'id' in request.json.get('content')
        assert 1 == request.json.get('content').get('id')
