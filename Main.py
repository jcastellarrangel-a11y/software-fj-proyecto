# Main.py
# Sistema de gestión de clientes, servicios y reservas
# Simula 10 operaciones válidas e inválidas

from Cliente import Cliente
from Sala import Sala
from Equipo import Equipo
from Asesoria import Asesoria
from Reserva import Reserva
from Logger import Logger
from Excepciones import *

def main():
    print("=" * 60)
    print("SISTEMA SOFTWARE FJ - GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS")
    print("=" * 60)
    
    Logger.registrar_info("=== INICIO DEL SISTEMA ===")
    
    # ========================================
    # OPERACIÓN 1: Cliente válido
    # ========================================
    print("\n--- OPERACIÓN 1: Crear cliente válido ---")
    try:
        cliente1 = Cliente("Ana Lopez", "ana@mail.com", "3123456789")
        print(f"Cliente creado: {cliente1.mostrar_info()}")
        Logger.registrar_info(f"Cliente creado: {cliente1.mostrar_info()}")
    except ClienteInvalidoError as e:
        print(f"Error: {e}")
        Logger.registrar_error(f"Error creando cliente: {e}")
    
    # ========================================
    # OPERACIÓN 2: Cliente con email inválido
    # ========================================
    print("\n--- OPERACIÓN 2: Cliente con email inválido ---")
    try:
        cliente2 = Cliente("Pedro Gomez", "correo-malo", "3209876543")
        print(f"Cliente creado: {cliente2.mostrar_info()}")
    except EmailInvalidoError as e:
        print(f"Error esperado: {e}")
        Logger.registrar_error(f"Email inválido: {e}")
    
    # ========================================
    # OPERACIÓN 3: Cliente con teléfono inválido
    # ========================================
    print("\n--- OPERACIÓN 3: Cliente con teléfono inválido ---")
    try:
        cliente3 = Cliente("Maria Ruiz", "maria@mail.com", "123")
        print(f"Cliente creado: {cliente3.mostrar_info()}")
    except TelefonoInvalidoError as e:
        print(f"Error esperado: {e}")
        Logger.registrar_error(f"Teléfono inválido: {e}")
    
    # ========================================
    # OPERACIÓN 4: Cliente con nombre vacío
    # ========================================
    print("\n--- OPERACIÓN 4: Cliente con nombre vacío ---")
    try:
        cliente4 = Cliente("", "vacio@mail.com", "3188888888")
        print(f"Cliente creado: {cliente4.mostrar_info()}")
    except ClienteInvalidoError as e:
        print(f"Error esperado: {e}")
        Logger.registrar_error(f"Nombre vacío: {e}")
    
    # ========================================
    # OPERACIÓN 5: Crear servicio Sala
    # ========================================
    print("\n--- OPERACIÓN 5: Crear servicio Sala ---")
    try:
        sala1 = Sala("Sala de Conferencias", 30, 100000)
        print(f"Servicio creado: {sala1.describir()}")
        Logger.registrar_info(f"Servicio Sala creado: {sala1.nombre}")
    except Exception as e:
        print(f"Error: {e}")
        Logger.registrar_error(f"Error creando Sala: {e}")
    
    # ========================================
    # OPERACIÓN 6: Crear servicio Equipo
    # ========================================
    print("\n--- OPERACIÓN 6: Crear servicio Equipo ---")
    try:
        equipo1 = Equipo("Proyector Epson", "Proyector", 50000)
        print(f"Servicio creado: {equipo1.describir()}")
        Logger.registrar_info(f"Servicio Equipo creado: {equipo1.nombre}")
    except Exception as e:
        print(f"Error: {e}")
        Logger.registrar_error(f"Error creando Equipo: {e}")
    
    # ========================================
    # OPERACIÓN 7: Crear servicio Asesoría
    # ========================================
    print("\n--- OPERACIÓN 7: Crear servicio Asesoría ---")
    try:
        asesoria1 = Asesoria("Python Avanzado", "Programación", 80000)
        print(f"Servicio creado: {asesoria1.describir()}")
        Logger.registrar_info(f"Servicio Asesoría creado: {asesoria1.nombre}")
    except Exception as e:
        print(f"Error: {e}")
        Logger.registrar_error(f"Error creando Asesoría: {e}")
    
    # ========================================
    # OPERACIÓN 8: Reserva exitosa
    # ========================================
    print("\n--- OPERACIÓN 8: Reserva exitosa ---")
    try:
        if 'cliente1' in locals() and 'sala1' in locals():
            reserva1 = Reserva(cliente1, sala1, 3)
            costo = reserva1.confirmar()
            print(f"Reserva confirmada. Costo: ${costo}")
            print(f"   {reserva1.mostrar()}")
            Logger.registrar_info(f"Reserva exitosa - Costo: ${costo}")
        else:
            print("No hay cliente o servicio disponible")
    except Exception as e:
        print(f"Error: {e}")
        Logger.registrar_error(f"Error en reserva exitosa: {e}")
    
    # ========================================
    # OPERACIÓN 9: Reserva con servicio inválido
    # ========================================
    print("\n--- OPERACIÓN 9: Reserva con servicio inválido ---")
    try:
        if 'cliente1' in locals():
            reserva2 = Reserva(cliente1, None, 2)
            costo = reserva2.confirmar()
            print(f"Reserva confirmada. Costo: ${costo}")
        else:
            print("No hay cliente disponible")
    except ServicioNoDisponibleError as e:
        print(f"Error esperado: {e}")
        Logger.registrar_error(f"Reserva con servicio inválido: {e}")
    except Exception as e:
        print(f"Error: {e}")
        Logger.registrar_error(f"Error inesperado: {e}")
    
    # ========================================
    # OPERACIÓN 10: Cancelar una reserva
    # ========================================
    print("\n--- OPERACIÓN 10: Cancelar reserva ---")
    try:
        if 'reserva1' in locals():
            reserva1.cancelar()
            print(f"Reserva cancelada: {reserva1.mostrar()}")
            Logger.registrar_info(f"Reserva cancelada exitosamente")
        else:
            print("No hay reserva para cancelar")
    except Exception as e:
        print(f"Error: {e}")
        Logger.registrar_error(f"Error cancelando reserva: {e}")
    
    # ========================================
    # RESUMEN FINAL
    # ========================================
    print("\n" + "=" * 60)
    print("RESUMEN FINAL")
    print("=" * 60)
    print("Sistema ejecutado sin caídas gracias al manejo de excepciones")
    print("Revisa el archivo 'logs.txt' para ver todos los eventos registrados")
    print("=" * 60)
    
    Logger.registrar_info("=== FIN DEL SISTEMA ===")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        Logger.registrar_error(f"Error crítico en el sistema: {e}")
        print(f"Error crítico: {e}")
    finally:
        print("\nSistema finalizado sin interrupciones.")