# servicio.py
# Clase abstracta Servicio
from abc import ABC, abstractmethod

class Servicio(ABC):
    """Clase abstracta que define la plantilla para todos los servicios"""
    
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    @abstractmethod
    def calcular_costo(self, duracion=1, **kwargs):
        """Calcula el costo del servicio"""
        pass
    
    @abstractmethod
    def describir(self):
        """Devuelve una descripción del servicio"""
        pass
    
    @abstractmethod
    def validar(self):
        """Valida que los datos del servicio sean correctos"""
        pass
    
    def __str__(self):
        return f"{self.tipo}: {self.nombre}"