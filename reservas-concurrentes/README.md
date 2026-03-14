# Simulación de Reservas Concurrentes

Este proyecto simula múltiples usuarios intentando reservar asientos al mismo tiempo usando Python y threading.

## Problema

Cuando varios procesos acceden al mismo recurso compartido al mismo tiempo puede ocurrir una condición de carrera (race condition), generando datos inconsistentes.

Ejemplo: múltiples usuarios reservando los mismos asientos.

## Parte 1: Sin Lock

Se implementa la simulación sin ningún mecanismo de control de concurrencia.

Resultado:
Puede generar asientos negativos debido a que varios hilos modifican la variable al mismo tiempo.

## Parte 2: Con Lock

Se utiliza un Lock para proteger la sección crítica.

Resultado:
Solo un hilo puede modificar los asientos a la vez, evitando inconsistencias.

## Parte 3: Con Semáforo

Se utiliza un semáforo para permitir hasta 3 reservas simultáneas.

Resultado:
Controla el número de accesos concurrentes al recurso compartido.

## Conclusión

Los mecanismos de sincronización como Lock y Semáforos permiten evitar problemas de concurrencia en sistemas donde múltiples procesos acceden a recursos compartidos.