# Simulación de Reservas Concurrentes
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python Logo" width="300"/>

Este proyecto simula múltiples usuarios intentando reservar asientos al mismo tiempo usando Python y threading.

# Simulación de Reservas Concurrentes

**Demostración de concurrencia, Race Conditions y sincronización con Python**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Threading](https://img.shields.io/badge/Threading-Módulo_Estándar-FFD43B?style=for-the-badge&logo=python&logoColor=black)
![License](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Estado-Completado-success?style=for-the-badge)
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
