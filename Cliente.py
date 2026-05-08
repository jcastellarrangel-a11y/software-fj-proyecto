from excepciones import DatoInvalidoError

class Cliente:
    def __init__(self, nombre, identificacion, correo):
        self.set_nombre(nombre)
        self.set_identificacion(identificacion)
        self.set_correo(correo)

    # Encapsulación
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if not nombre or not isinstance(nombre, str):
            raise DatoInvalidoError("Nombre inválido")
        self.__nombre = nombre

    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        if not identificacion or len(str(identificacion)) < 5:
            raise DatoInvalidoError("Identificación inválida")
        self.__identificacion = identificacion

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        if "@" not in correo:
            raise DatoInvalidoError("Correo inválido")
        self.__correo = correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | ID: {self.__identificacion} | Correo: {self.__correo}"
