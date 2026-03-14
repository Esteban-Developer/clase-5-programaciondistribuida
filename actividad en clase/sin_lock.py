import threading

asientos = 10

def reservar():
    global asientos

    if asientos > 0:
        asientos -= 1
        print("Reserva realizada. Asientos restantes:", asientos)

hilos = []

for i in range(50):
    hilo = threading.Thread(target=reservar)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Asientos finales:", asientos)