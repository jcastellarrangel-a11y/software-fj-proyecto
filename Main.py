from cliente import Cliente
from reserva import Reserva
from sala import Sala
from equipo import Equipo
from asesoria import Asesoria
from logger import Logger

def main():
    clientes = []
    reservas = []

    # PRUEBAS (válidas e inválidas)
    operaciones = [
        lambda: Cliente("Juan", "12345", "juan@gmail.com"),
        lambda: Cliente("", "123", "malcorreo"),  # inválido
        lambda: Cliente("Ana", "67890", "ana@gmail.com"),
    ]

    # CREAR CLIENTES
    for op in operaciones:
        try:
            cliente = op()
            clientes.append(cliente)
            print("Cliente creado:", cliente.mostrar_info())
        except Exception as e:
            Logger.log(f"Error creando cliente: {str(e)}")

    # CREAR SERVICIOS
    try:
        sala = Sala("Sala VIP", 50000)
        equipo = Equipo("Proyector", 30000)
        asesoria = Asesoria("Consultoría", 80000)
    except Exception as e:
        Logger.log(f"Error creando servicios: {str(e)}")

    # CREAR RESERVAS
    try:
        r1 = Reserva(clientes[0], sala, 2)
        reservas.append(r1)

        r2 = Reserva(clientes[1], equipo, -1)  # inválido
        reservas.append(r2)

        r3 = Reserva(clientes[0], asesoria, 1)
        reservas.append(r3)

    except Exception as e:
        Logger.log(f"Error creando reservas: {str(e)}")

    # PROCESAR RESERVAS
    for r in reservas:
        try:
            costo = r.confirmar()
            print(f"Reserva confirmada. Costo: {costo}")
        except Exception as e:
            Logger.log(f"Error procesando reserva: {str(e)}")

    # CANCELACIÓN DE PRUEBA
    try:
        reservas[0].cancelar()
    except Exception as e:
        Logger.log(str(e))

    print("\nEstado final de reservas:")
    for r in reservas:
        try:
            print(r.mostrar())
        except:
            pass


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        Logger.log(f"Error crítico en el sistema: {str(e)}")
    finally:
        print("Sistema finalizado sin interrupciones.")
