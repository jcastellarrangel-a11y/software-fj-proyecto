# logger.py
import datetime

class Logger:
    @staticmethod
    def registrar_evento(mensaje, tipo="INFO"):
        try:
            with open("logs.txt", "a", encoding="utf-8") as archivo:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                archivo.write(f"[{timestamp}] [{tipo}] {mensaje}\n")
        except Exception as e:
            print(f"Error al escribir en log: {e}")
    
    @staticmethod
    def registrar_error(mensaje):
        Logger.registrar_evento(mensaje, "ERROR")
    
    @staticmethod
    def registrar_info(mensaje):
        Logger.registrar_evento(mensaje, "INFO")
