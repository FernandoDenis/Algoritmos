# Realizando Cache Least Recently use

import time

class LRUCache:
    # Se utiliza para obtener el indice del hijo izquierdo de un nodo que sea padre
    def hijoIzq(self,idx):
        return (idx * 2) + 1
    
    def hijoDer(self,idx):
        return (idx * 2) + 2
    
    # Funcion bubble
    def bubble(self, idxActual, limit):
        # Se le suma 1 al indice actual para arreglar el problema de la formula cuando el indice es 1 (1  * 2 = 2 (2 NO ES EL HIJO DE 1))
        while (self.hijoIzq(idxActual)) < limit:
            # Guardamos el valor del cache para intercambiar indices por medio de "desempaquetamiento de tuplas"
            # El cache modifica su valor por medio de su key que toma del id, por eso esta el numero 2, ya que esa es la posicion del id en la estructura de array
            idActual = self.memory[idxActual][2]
            # El id del nodo izquierdo a intercambiar
            idIzq = self.memory[self.hijoIzq(idxActual)][2]
            # El id del nodo derecho a intercambiar
            idDer = self.memory[self.hijoDer(idxActual)][2]
            
            # Se decide que hijo es el que lleva mas tiempo y lo movemos hasta adelante ya que es el mas reciente
            if self.memory[self.hijoDer(idxActual)][1] > self.memory[self.hijoIzq(idxActual) ][1]:
                # Cambiamos de posicion en el cache usando los ids
                self.cache[idActual], self.cache[idIzq] = self.cache[idIzq], self.cache[idActual]
                # Cambio de posicion en la memoria (array)
                self.memory[idxActual],self.memory[self.hijoIzq(idxActual)] = self.memory[self.hijoIzq(idxActual)], self.memory[idxActual]
                idxActual = self.hijoIzq(idxActual)
            else:
                self.cache[idActual], self.cache[idDer] = self.cache[idDer], self.cache[idActual]
                
                self.memory[idxActual],self.memory[self.hijoDer(idxActual)] = self.memory[self.hijoDer(idxActual)], self.memory[idxActual]
                idxActual = self.hijoDer(idxActual)
    
    def __init__(self, size):
        # Mapa donde contendra guardado la posicion de cada dato
        self.cache = dict()
        self.limit = size
        self.memory = []
        # indice para asignar indice al mapa
        self.idx = 0
    
    def put(self, id, value):
        # Aseguramos que el id no se encuentre ya en el cache
        if id in self.cache:
            self.get(id)
            return
        
        # Revisamos si el cache esta lleno o no, para poder agregar elementos sin tener que quitar ninguo
        if len(self.memory) < self.limit:
            self.cache[id] = self.idx
            self.idx += 1
            self.memory.append([value, time.time(), id])
            return        
        else: 
            # Eliminamos el elemento mas viejo
            delElement = self.memory.pop(0)
            # Elimino el elemento del cache por medio de su id
            del self.cache[delElement[2]]
            
            # Agregamos el nuevo elemento en la posicion donde quitamos el elementos
            self.memory.insert(0 ,[value, time.time(), id])
            # El id es el key del diccionario y su valor es 0 porque fue agregado al inicio del array
            self.cache[id] = 0
            
            actualIdx = 0
            
            # Acomoda el elemento agregado posicinandolo como el mas viejo
            self.bubble(actualIdx, self.limit)
        return

    def get(self, id):
        if id in self.cache:
            
            # Guardar el indice del id que se quiere buscar
            actualIdx = self.cache[id]
            
            self.memory[actualIdx][1] = time.time()
            
            if actualIdx == 0 and len(self.memory) == 2:
                # Estoy utilizando dos variables para intercambiar dos valores de valor al mismo tiempo
                idActual = self.memory[actualIdx][2]
                idCambiar = self.memory[actualIdx + 1][2]
                
                self.cache[idActual], self.cache[idCambiar] = self.cache[idCambiar], self.cache[idActual]
                
                self.memory[actualIdx],self.memory[actualIdx + 1] = self.memory[actualIdx + 1], self.memory[actualIdx]
                return self.memory[actualIdx + 1][0]
            
            self.bubble(actualIdx, self.idx)
            
            # Devuelve el valor con el indice actualizado (Solo sirve para los pruebas)
            return self.memory[actualIdx][0]
        else:
            return -1
    
    def print(self):
        return self.memory
    
# newCache = LRUCache()
# newCache.put(34, 5)
# time.sleep(1)
# newCache.put(23, 7)
# time.sleep(1)
# newCache.put(32, 9)
# time.sleep(1)
# newCache.put(56, 1)
# time.sleep(1)
# newCache.put(65, 10)
# time.sleep(1)
# newCache.put(41, 67)
# time.sleep(1)
# newCache.put(59, 0)
# time.sleep(1)

# print(newCache.print())
# print(newCache.cache)
# print("Actualizar")
# newCache.get(34)
# newCache.get(23)
# newCache.get(32)
# newCache.get(56)
# newCache.get(65)
# newCache.get(41)
# print(newCache.print())
# print(newCache.cache)

# print(newCache.print())
# print(newCache.cache)
# newCache.put(1, 67)
# print(newCache.print())
# print(newCache.cache)
# newCache.put(2, 59)
# print(newCache.print())
# print(newCache.cache)
# newCache.put(868, 23)
# print(newCache.print())
# print(newCache.cache)
# newCache.put(432, 61)
# print(newCache.print())
# print(newCache.cache)
# newCache.put(62, 84)
# print(newCache.print())
# print(newCache.cache)
# newCache.put(29, 405)
# print(newCache.print())

# print(newCache.cache)

