# reserva.py
# Clase Reserva que integra cliente, servicio, duración y estado
from Excepciones import ReservaInvalidaError, ServicioNoDisponibleError
from Logger import Logger

class Reserva:
    """Clase que representa una reserva de un servicio por un cliente"""
    
    def __init__(self, cliente, servicio, duracion, estado="Pendiente"):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = estado
    
    def confirmar(self):
        """Confirma la reserva y calcula el costo"""
        try:
            if self.servicio is None:
                raise ServicioNoDisponibleError("El servicio no está disponible")
            
            if self.duracion <= 0:
                raise ReservaInvalidaError("La duración debe ser mayor a 0")
            
            if self.cliente is None:
                raise ReservaInvalidaError("El cliente no es válido")
            
            costo = self.servicio.calcular_costo(self.duracion)
            self.estado = "Confirmada"
            Logger.registrar_info(f"Reserva confirmada - Cliente: {self.cliente.nombre} - Servicio: {self.servicio.nombre} - Costo: ${costo}")
            return costo
            
        except Exception as e:
            Logger.registrar_error(f"Error al confirmar reserva: {e}")
            raise
    
    def cancelar(self):
        """Cancela la reserva"""
        try:
            if self.estado == "Cancelada":
                raise ReservaInvalidaError("La reserva ya estaba cancelada")
            
            self.estado = "Cancelada"
            Logger.registrar_info(f"Reserva cancelada - Cliente: {self.cliente.nombre} - Servicio: {self.servicio.nombre}")
            
        except Exception as e:
            Logger.registrar_error(f"Error al cancelar reserva: {e}")
            raise
    
    def mostrar(self):
        """Muestra la información de la reserva"""
        estado_str = self.estado
        servicio_str = self.servicio.nombre if self.servicio else "Servicio no disponible"
        return f"Reserva: {self.cliente.nombre} - {servicio_str} - {self.duracion} horas - Estado: {estado_str}"
    
    def __str__(self):
        return self.mostrar()