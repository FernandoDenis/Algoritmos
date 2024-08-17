
import heapq

import time

import random

#Array donde van a estar todas las alarmas
alarmas = []

#Ciclo para agregar 10,000 alarmas aleatorias y agregarlas en el array "alarmas"
for i in range(10000):
    #Estructura que suma un numero random entre un rango de -+100,000 para que agregue alarmas que ya hayan pasado y otras que no
    alarma = (f"Alarma{i}", int(time.time()) + random.randint(-100000,100000))
    alarmas.append(alarma)


#Ordena de menor a mayor el array alarmas para tener control del tiempo de las alarmas
alarmas = heapq.nsmallest(len(alarmas), alarmas, key=lambda x: x[1])

# #Saca las alarmas hasta llegar a la del tiempo actual
while(alarmas[0][1] < int(time.time())):
    alarmas.pop(0)

#Imprime las 5 alarmas que siguen
print(heapq.nsmallest(5,alarmas,key=lambda x: x[1]))