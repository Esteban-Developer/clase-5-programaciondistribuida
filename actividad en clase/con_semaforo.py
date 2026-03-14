import threading

asientos = 10
semaforo = threading.Semaphore(3)  # máximo 3 usuarios al mismo tiempo

def reservar():
    global asientos

    with semaforo:  # sección controlada por semáforo

        if asientos > 0:
            asientos -= 1
            print("Reserva realizada. Asientos restantes:", asientos)
        else:
            print("No hay asientos disponibles")


hilos = []

for i in range(50):
    hilo = threading.Thread(target=reservar)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Asientos finales:", asientos)