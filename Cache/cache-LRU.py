# Realizando Cache Least Recently use

import time

class LRUCache:
    def __init__(self):
        # Mapa donde contendra guardado la posicion de cada dato
        self.cache = dict()
        self.limit = 7
        self.memory = []
        
    def get(self, id, value):
        # Aseguramos que el id no se encuentre ya en el cache
        if id in self.cache:
            self.update(id)
            return
        
        # Revisamos si el cache esta lleno o no, para poder agregar elementos sin tener que quitar ninguo
        if len(self.memory) < self.limit:
            self.cache[id] = value
            self.memory.append((id, time.time()))
            return        
        else: 
            # Eliminamos el elemento mas viejo
            self.memory.pop(0)
            
            # Agregamos el nuevo elemento en la posicion donde no hay elementos
            self.memory.insert(0 ,(id, time.time()))
            
            # Se decide que hijo es el que lleva mas tiempo y lo movemos hasta adelante ya que es el mas reciente
            if self.memory[1][1] > self.memory[2][1]:
                self.memory[0],self.memory[2] = self.memory[2], self.memory[0]
                idxActual = 2
            else:
                self.memory[0],self.memory[1] = self.memory[1], self.memory[0]
                idxActual = 1
            
            while ((idxActual + 1) * 2) < self.limit:
                if self.memory[((idxActual + 1) * 2) - 1][1] > self.memory[(idxActual + 1) * 2 ][1]:
                    self.memory[idxActual],self.memory[(idxActual + 1) * 2] = self.memory[(idxActual + 1) * 2], self.memory[idxActual]
                    idxActual = (idxActual + 1) * 2
                else:
                    self.memory[idxActual],self.memory[((idxActual + 1) * 2) - 1] = self.memory[((idxActual + 1) * 2) - 1], self.memory[idxActual]
                    idxActual = ((idxActual + 1) * 2) - 1

    def update(self, id):
        if id in self.cache:
            for data in self.memory:
                if id == data[1]:
                    data = (id, time.time())
                    return
            return
        else:
            return
    
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
print(newCache.print())
newCache.get(1, 67)
print(newCache.print())
newCache.get(2, 59)
print(newCache.print())
newCache.get(868, 23)
print(newCache.print())
newCache.get(432, 61)
print(newCache.print())
newCache.get(62, 84)
print(newCache.print())
newCache.get(29, 405)
print(newCache.print())



# cash = dict()
# cash[1] = "Homero"
# print(cash)

# casa = ["XD", "DX", "LA"]
# casa.insert(0,"1")

# print(casa)

# print(casa.pop(0))