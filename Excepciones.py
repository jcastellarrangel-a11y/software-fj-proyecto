# excepciones.py
# Excepciones personalizadas para el sistema

class ClienteInvalidoError(Exception):
    """Error cuando los datos del cliente no son válidos"""
    pass

class ServicioNoDisponibleError(Exception):
    """Error cuando el servicio solicitado no está disponible"""
    pass

class ReservaInvalidaError(Exception):
    """Error cuando la reserva no se puede realizar"""
    pass

class DatosFaltantesError(Exception):
    """Error cuando faltan parámetros obligatorios"""
    pass

class EmailInvalidoError(ClienteInvalidoError):
    """Error específico para email inválido"""
    pass

class TelefonoInvalidoError(ClienteInvalidoError):
    """Error específico para teléfono inválido"""
    pass