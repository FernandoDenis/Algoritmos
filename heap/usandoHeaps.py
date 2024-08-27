
import heapq

import time

import random

# Array donde van a estar todas las alarmas
alarmas = []

# Ciclo para agregar 10,000 alarmas aleatorias y agregarlas en el array "alarmas"
for i in range(10000):
    # Estructura que suma un numero random entre un rango de -+100,000 para que agregue alarmas que ya hayan pasado y otras que no
    alarma = (int(time.time()) + random.randint(-100000,100000) , f"Alarma{i}")
    heapq.heappush(alarmas, alarma)

# Saca las alarmas hasta llegar a la del tiempo actual
while(alarmas[0][0] < int(time.time())):
    heapq.heappop(alarmas)

# La alarma que sigue
print(alarmas[0])
