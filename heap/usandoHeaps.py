
import heapq

import time

import random

#Array donde van a estar todas las alarmas
alarmas = []

#Array donde van a estar solo las alarmas que no hayan pasado
restAlarmas = []

#Variable donde se guarda el epoch actual para poder trabajar con el mismo valor al crear las alarmas
epoch_actual = int(time.time())

#Ciclo para agregar 10,000 alarmas aleatorias y agregarlas en el array "alarmas"
for i in range(10000):
    #Se suma un numero random entre un rango de -+100,000 para que agregue alarmas que ya hayan pasado y otras que no
    alarmas.append(epoch_actual + random.randint(-100000,100000))

#Ciclo para eliminar las alarmas que ya hayan pasado y solo queden las que faltan en el futuro
for i in alarmas:
    if (i - epoch_actual) >= 0:
        restAlarmas.append(i)

#Heap para mostrar las proximas 5 alarmas que van a sonar en un futuro
print(heapq.nsmallest(5, restAlarmas))