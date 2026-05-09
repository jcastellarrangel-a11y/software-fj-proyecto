# asesoria.py
from servicio import Servicio

class Asesoria(Servicio):
    def __init__(self, nombre, especialidad, costo_por_hora=50000):
        super().__init__(nombre, "Asesoria")
        self.especialidad = especialidad
        self.costo_por_hora = costo_por_hora
    
    def calcular_costo(self, duracion_horas=1, **kwargs):
        return duracion_horas * self.costo_por_hora
    
    def describir(self):
        return f"Asesoría de {self.nombre} - Especialidad: {self.especialidad} - ${self.costo_por_hora}/hora"
    
    def validar(self):
        return len(self.nombre) > 0 and len(self.especialidad) > 0