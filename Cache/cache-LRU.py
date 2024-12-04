# Realizando Cache Least Recently use

import time

class LRUCache:
    def __init__(self):
        # Mapa donde contendra guardado la posicion de cada dato
        self.cache = dict()
        self.limit = 7
        self.memory = []
        # indice para asignar indice al mapa
        self.idx = 0
        
    def get(self, id, value):
        # Aseguramos que el id no se encuentre ya en el cache
        if id in self.cache:
            self.update(id)
            return
        
        # Revisamos si el cache esta lleno o no, para poder agregar elementos sin tener que quitar ninguo
        if len(self.memory) < self.limit:
            self.cache[id] = self.idx
            self.idx += 1
            self.memory.append((value, time.time(), id))
            return        
        else: 
            # Eliminamos el elemento mas viejo
            delElement = self.memory.pop(0)
            # Elimino el elemento del cache por medio de su id
            del self.cache[delElement[2]]
            
            # Agregamos el nuevo elemento en la posicion donde quitamos el elementos
            self.memory.insert(0 ,(value, time.time(), id))
            # Se agrega el nuevo elemento al cache
            self.cache[id] = 0
            
            # Se decide que hijo es el que lleva mas tiempo y lo movemos hasta adelante ya que es el mas reciente
            if self.memory[1][1] > self.memory[2][1]:
                # Cambiamos de posicion en el cache usando los ids
                self.cache[self.memory[0][2]], self.cache[self.memory[2][2]] = self.cache[self.memory[2][2]],  self.cache[self.memory[0][2]]
                # Cambio de posicion en la memoria (array)
                self.memory[0],self.memory[2] = self.memory[2], self.memory[0]
                idxActual = 2
            else:
                self.cache[self.memory[0][2]], self.cache[self.memory[1][2]] = self.cache[self.memory[1][2]], self.cache[self.memory[0][2]]
                
                self.memory[0],self.memory[1] = self.memory[1], self.memory[0]
                idxActual = 1
            
            # Se le suma 1 al indice actual para arreglar el problema de la formula cuando el indice es 1 (1  * 2 = 2 (2 NO ES EL HIJO DE 1))
            while ((idxActual + 1) * 2) < self.limit:
                if self.memory[((idxActual + 1) * 2) - 1][1] > self.memory[(idxActual + 1) * 2 ][1]:
                    self.cache[self.memory[idxActual][2]], self.cache[self.memory[(idxActual + 1) * 2][2]] = self.cache[self.memory[(idxActual + 1) * 2][2]], self.cache[self.memory[idxActual][2]]
                
                    self.memory[idxActual],self.memory[(idxActual + 1) * 2] = self.memory[(idxActual + 1) * 2], self.memory[idxActual]
                    idxActual = (idxActual + 1) * 2
                else:
                    self.cache[self.memory[idxActual][2]], self.cache[self.memory[((idxActual + 1) * 2) - 1][2]] = self.cache[self.memory[((idxActual + 1) * 2) - 1][2]], self.cache[self.memory[idxActual][2]]
                
                    self.memory[idxActual],self.memory[((idxActual + 1) * 2) - 1] = self.memory[((idxActual + 1) * 2) - 1], self.memory[idxActual]
                    idxActual = ((idxActual + 1) * 2) - 1
        return

    def update(self, id):
        if id in self.cache:
            
            # Guardar el indice del id que se quiere buscar
            idxActual = self.cache[id]
            
            if idxActual == 0:
                if self.memory[1][1] > self.memory[2][1]:
                    # Cambiamos de posicion en el cache usando los ids
                    self.cache[self.memory[0][2]], self.cache[self.memory[2][2]] = self.cache[self.memory[2][2]],  self.cache[self.memory[0][2]]
                    # Cambio de posicion en la memoria (array)
                    self.memory[0],self.memory[2] = self.memory[2], self.memory[0]
                    idxActual = 2
                else:
                    self.cache[self.memory[0][2]], self.cache[self.memory[1][2]] = self.cache[self.memory[1][2]], self.cache[self.memory[0][2]]
                
                    self.memory[0],self.memory[1] = self.memory[1], self.memory[0]
                    idxActual = 1
            
            while ((idxActual + 1) * 2) < self.limit:
                if self.memory[((idxActual + 1) * 2) - 1][1] > self.memory[(idxActual + 1) * 2 ][1]:
                    self.cache[self.memory[idxActual][2]], self.cache[self.memory[(idxActual + 1) * 2][2]] = self.cache[self.memory[(idxActual + 1) * 2][2]], self.cache[self.memory[idxActual][2]]
                
                    self.memory[idxActual],self.memory[(idxActual + 1) * 2] = self.memory[(idxActual + 1) * 2], self.memory[idxActual]
                    idxActual = (idxActual + 1) * 2
                else:
                    self.cache[self.memory[idxActual][2]], self.cache[self.memory[((idxActual + 1) * 2) - 1][2]] = self.cache[self.memory[((idxActual + 1) * 2) - 1][2]], self.cache[self.memory[idxActual][2]]
                
                    self.memory[idxActual],self.memory[((idxActual + 1) * 2) - 1] = self.memory[((idxActual + 1) * 2) - 1], self.memory[idxActual]
                    idxActual = ((idxActual + 1) * 2) - 1
        else:
            return -1
    
    def print(self):
        return self.memory
    
newCache = LRUCache()
newCache.get(34, 5)
time.sleep(1)
newCache.get(23, 7)
time.sleep(1)
newCache.get(32, 9)
time.sleep(1)
newCache.get(56, 1)
time.sleep(1)
newCache.get(65, 10)
time.sleep(1)
newCache.get(41, 67)
time.sleep(1)
newCache.get(59, 0)
time.sleep(1)

# print(newCache.print())
# print(newCache.cache)

# print("Actualizar")
# newCache.update(34)
# newCache.update(23)
# newCache.update(32)
# newCache.update(56)
# newCache.update(65)
# newCache.update(41)
# print(newCache.print())
# print(newCache.cache)

print(newCache.print())
print(newCache.cache)
newCache.get(1, 67)
print(newCache.print())
print(newCache.cache)
newCache.get(2, 59)
print(newCache.print())
print(newCache.cache)
newCache.get(868, 23)
print(newCache.print())
print(newCache.cache)
newCache.get(432, 61)
print(newCache.print())
print(newCache.cache)
newCache.get(62, 84)
print(newCache.print())
print(newCache.cache)
newCache.get(29, 405)
print(newCache.print())

print(newCache.cache)

