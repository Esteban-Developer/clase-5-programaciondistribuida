import threading

asientos = 10
sem = threading.Semaphore(3)

def reservar():
    global asientos

    with sem:
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