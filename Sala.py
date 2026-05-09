from servicio import Servicio

class Sala(Servicio):

    def __init__(self, nombre, precio_base):
        super().__init__(nombre, precio_base)
        self.tipo = "Sala de reuniones"

# ------------------Polimorfismo------------------
    def calcular_costo(self, horas):

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")

        return self.get_precio_base() * horas

    def descripcion(self):

        return (
            f"Servicio de Sala\n"
            f"Nombre: {self.get_nombre()}\n"
            f"Tipo: {self.tipo}\n"
            f"Precio por hora: ${self.get_precio_base()}"
        )
