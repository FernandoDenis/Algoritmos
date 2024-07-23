#Implementando un stack usando queues

class Queues:
    def __init__(self):
        self.queue = []
        
    def push(self,data):
        self.queue.append(data)
        
    def shift(self):
        first_value = self.queue[0]
        for i in range(len(self.queue) - 1):
            self.queue[i] = self.queue[i + 1]
        self.queue.pop()
        return first_value
            
    def print(self):
        print(self.queue)
        
#Implementar un stack
cola = Queues()

cola.push(1)
cola.push(2)
cola.push(3)
cola.push(4)
cola.push(5)

cola.print()
print("\n\n")

#Funcion para eliminar el ultimo elemento de un queue usando queues

def popQueues(queues):
    cola2 = Queues()
    
    for i in range(len(queues.queue) - 1):
        cola2.push(queues.shift())
    queues.shift()
    
    for i in range(len(cola2.queue)):
        queues.push(cola2.shift())
    
popQueues(cola)
cola.print()
