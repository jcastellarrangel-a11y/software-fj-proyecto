# cliente.py
# Clase Cliente con validaciones robustas
import re
from Excepciones import ClienteInvalidoError, EmailInvalidoError, TelefonoInvalidoError

class Cliente:
    """Clase que representa un cliente con validaciones"""
    
    def __init__(self, nombre, email, telefono):
        self._nombre = None
        self._email = None
        self._telefono = None
        
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 2:
            raise ClienteInvalidoError("El nombre debe tener al menos 2 caracteres")
        self._nombre = valor.strip()
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, valor):
            raise EmailInvalidoError(f"El email '{valor}' no es válido")
        self._email = valor.strip()
    
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor):
        if not valor or len(valor) < 7 or len(valor) > 15:
            raise TelefonoInvalidoError(f"El teléfono '{valor}' no es válido. Debe tener entre 7 y 15 dígitos")
        self._telefono = valor.strip()
    
    def mostrar_info(self):
        """Devuelve la información del cliente"""
        return f"Cliente: {self.nombre} - Email: {self.email} - Teléfono: {self.telefono}"
    
    def __str__(self):
        return self.mostrar_info()
