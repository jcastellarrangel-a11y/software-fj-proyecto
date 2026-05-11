# equipo.py
# Servicio de alquiler de equipos
from Servicio import Servicio

class Equipo(Servicio):
    """Clase que representa un equipo para alquilar"""
    
    def __init__(self, nombre, tipo_equipo, costo_por_dia):
        super().__init__(nombre, "Equipo")
        self.tipo_equipo = tipo_equipo
        self.costo_por_dia = costo_por_dia
    
    def calcular_costo(self, duracion_dias=1, **kwargs):
        """Calcula el costo de alquilar el equipo"""
        return duracion_dias * self.costo_por_dia
    
    def describir(self):
        """Devuelve una descripción del equipo"""
        return f"Equipo: {self.nombre} - Tipo: {self.tipo_equipo} - ${self.costo_por_dia}/día"
    
    def validar(self):
        """Valida que los datos del equipo sean correctos"""
        return len(self.nombre) > 0 and len(self.tipo_equipo) > 0 and self.costo_por_dia > 0
    
    def calcular_costo_con_impuesto(self, duracion_dias, impuesto=19):
        """Calcula costo con impuesto (polimorfismo)"""
        costo_base = self.calcular_costo(duracion_dias)
        return costo_base + (costo_base * impuesto / 100)
    
    def __str__(self):
        return f"Equipo: {self.nombre} ({self.tipo_equipo})"
