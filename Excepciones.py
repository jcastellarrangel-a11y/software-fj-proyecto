# excepciones.py

class ClienteInvalidoError(Exception):
    pass

class ServicioNoDisponibleError(Exception):
    pass

class ReservaInvalidaError(Exception):
    pass

class DatosFaltantesError(Exception):
    pass

class EmailInvalidoError(ClienteInvalidoError):
    pass

class TelefonoInvalidoError(ClienteInvalidoError):
    pass