# asesoria.py
# Servicio de asesorías especializadas
from Servicio import Servicio

class Asesoria(Servicio):
    """Clase que representa una asesoría especializada"""
    
    def __init__(self, nombre, especialidad, costo_por_hora=50000):
        super().__init__(nombre, "Asesoria")
        self.especialidad = especialidad
        self.costo_por_hora = costo_por_hora
    
    def calcular_costo(self, duracion_horas=1, **kwargs):
        """Calcula el costo total de la asesoría"""
        return duracion_horas * self.costo_por_hora
    
    def describir(self):
        """Devuelve una descripción de la asesoría"""
        return f"Asesoría de {self.nombre} - Especialidad: {self.especialidad} - ${self.costo_por_hora}/hora"
    
    def validar(self):
        """Valida que los datos de la asesoría sean correctos"""
        return len(self.nombre) > 0 and len(self.especialidad) > 0 and self.costo_por_hora > 0
    
    def aplicar_descuento(self, duracion_horas, porcentaje_descuento):
        """Calcula costo con descuento (polimorfismo)"""
        costo_base = self.calcular_costo(duracion_horas)
        descuento = costo_base * (porcentaje_descuento / 100)
        return costo_base - descuento
    
    def __str__(self):
        return f"Asesoria: {self.nombre} ({self.especialidad})"