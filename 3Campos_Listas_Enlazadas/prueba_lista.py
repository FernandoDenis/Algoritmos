#6:55

import random
from listas_tres_campos import LinkedList, Node

#Creando 10000 datos dentro y agregandolas a la lista
lista = LinkedList()
for i in range(1,10000 + 1):
    edad = random.randint(1,120)
    dinero = random.randint(0,10000)
    nombre = "Bot" + str(random.randint(0,100000))
    lista.agregar(i,edad,dinero,nombre)

#Realizando busqueda de 500 elementos
for i in range(1,500):
    print(lista.buscarElemento(random.randint(1,10000)))