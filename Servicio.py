from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if not nombre:
            raise ValueError("Nombre inválido")

        if precio_base <= 0:
            raise ValueError("Precio inválido")

        self._nombre = nombre
        self._precio_base = precio_base

    # Encapsulación
    def get_nombre(self):
        return self._nombre

    def get_precio_base(self):
        return self._precio_base

    # Métodos abstractos
    @abstractmethod
    def calcular_costo(self, tiempo):
        pass

    @abstractmethod
    def descripcion(self):
        pass
      
