# sala.py
# Servicio de reserva de salas
from Servicio import Servicio

class Sala(Servicio):
    """Clase que representa una sala para reservar"""
    
    def __init__(self, nombre, capacidad, costo_por_hora):
        super().__init__(nombre, "Sala")
        self.capacidad = capacidad
        self.costo_por_hora = costo_por_hora
    
    def calcular_costo(self, duracion_horas=1, **kwargs):
        """Calcula el costo de reservar la sala"""
        return duracion_horas * self.costo_por_hora
    
    def describir(self):
        """Devuelve una descripción de la sala"""
        return f"Sala: {self.nombre} - Capacidad: {self.capacidad} personas - ${self.costo_por_hora}/hora"
    
    def validar(self):
        """Valida que los datos de la sala sean correctos"""
        return len(self.nombre) > 0 and self.capacidad > 0 and self.costo_por_hora > 0
    
    def aplicar_descuento(self, duracion_horas, porcentaje):
        """Calcula costo con descuento (polimorfismo)"""
        costo_base = self.calcular_costo(duracion_horas)
        return costo_base - (costo_base * porcentaje / 100)
    
    def __str__(self):
        return f"Sala: {self.nombre} (Capacidad: {self.capacidad})"

