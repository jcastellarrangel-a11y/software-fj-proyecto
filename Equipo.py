from servicio import Servicio

class Equipo(Servicio):

    def __init__(self, nombre, precio_base):
        super().__init__(nombre, precio_base)
        self.categoria = "Audiovisual"

# -----------------Polimorfismo-----------------
    def calcular_costo(self, dias):
        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0")
        return self.get_precio_base() * dias

    def descripcion(self):
        return (
            f"Servicio de Equipo\n"
            f"Nombre: {self.get_nombre()}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio por día: ${self.get_precio_base()}"
        )
