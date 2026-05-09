# logger.py
# Manejo de archivo de logs para registrar errores y eventos
import datetime

class Logger:
    """Clase para escribir mensajes en un archivo de logs"""
    
    @staticmethod
    def registrar_evento(mensaje, tipo="INFO"):
        """
        Escribe un mensaje en el archivo logs.txt
        tipo puede ser: "INFO", "ERROR", "WARNING"
        """
        try:
            with open("logs.txt", "a", encoding="utf-8") as archivo:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                archivo.write(f"[{timestamp}] [{tipo}] {mensaje}\n")
        except Exception as e:
            print(f"Error al escribir en el log: {e}")
    
    @staticmethod
    def registrar_error(mensaje):
        """Método corto para registrar errores"""
        Logger.registrar_evento(mensaje, "ERROR")
    
    @staticmethod
    def registrar_info(mensaje):
        """Método corto para registrar información"""
        Logger.registrar_evento(mensaje, "INFO")
    
    @staticmethod
    def registrar_advertencia(mensaje):
        """Método corto para registrar advertencias"""
        Logger.registrar_evento(mensaje, "WARNING")
