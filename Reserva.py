from excepciones import ReservaError
from logger import Logger

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"

    def confirmar(self):
        try:
            if self.estado != "PENDIENTE":
                raise ReservaError("La reserva ya fue procesada")

            costo = self.servicio.calcular_costo(self.duracion)

            if costo <= 0:
                raise ReservaError("Costo inválido")

            self.estado = "CONFIRMADA"
            Logger.log(f"Reserva confirmada para {self.cliente.get_nombre()}")

            return costo

        except Exception as e:
            Logger.log(f"Error al confirmar reserva: {str(e)}")
            raise ReservaError("No se pudo confirmar la reserva") from e

    def cancelar(self):
        try:
            if self.estado == "CANCELADA":
                raise ReservaError("La reserva ya está cancelada")

            self.estado = "CANCELADA"
            Logger.log(f"Reserva cancelada para {self.cliente.get_nombre()}")

        except Exception as e:
            Logger.log(f"Error al cancelar reserva: {str(e)}")
            raise

    def mostrar(self):
        return f"{self.cliente.get_nombre()} - {self.servicio.descripcion()} - Estado: {self.estado}"
