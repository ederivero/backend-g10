class ProductosController:
    def listarProductos(self):
        productos = [
            {
                'nombre': 'Zapatillas Nike',
                'precio': 200.00,
                'talla': 42
            },
            {
                'nombre': 'Zapatillas Pumba',
                'precio': 150.00,
                'talla': 41
            }
        ]
        return productos