from ..models.productos_model import ProductosModel

class ProductosController:

    def listarProductos(self):
        productos = ProductosModel.query.all()
        print(productos)
        return []