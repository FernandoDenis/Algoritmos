
#Cola circular

#Nodo 
class NodoQueue:
    def __init__(self, data, back):
        self.data = data
        self.next = None
        self.back = back
        
#Lista
class QueueList:
    def __init__(self):
        self.start = None
        self.end = None
        
    def push(self,data):
        #Compara cuando se inserta el primer elemento
        if(self.start == None):
            self.start = NodoQueue(data,self.end)
            #Al haber solo un elemento el final va a ser el principio
            self.end = self.start
            #El siguiente del inicio va a ser el final para que sea circular
            self.start.next = self.end
        else:
            actualNode = self.start
            #Ciclo para llegar al ultimo elemento
            while(actualNode != self.end):
                actualNode = actualNode.next
            actualNode.next = NodoQueue(data,actualNode)
            self.end = actualNode.next
            actualNode.next.next = self.start

    def pop(self):
        self.start = self.start.next
        self.end.next = self.start
                     
    def print(self):
        actualNode = self.start
        print(actualNode.data, end=" -> ")
        actualNode = actualNode.next
        while (actualNode != self.start):
            print(actualNode.data, end=" -> ")
            actualNode = actualNode.next

cola = QueueList()
cola.push(1)
cola.push(2)
cola.push(3)
cola.push(4)
cola.push(5)
cola.push(6)
cola.push(7)
cola.push(8)
cola.push(9)
cola.push(10)

cola.pop()
cola.pop()
cola.pop()
cola.pop()


cola.print()
        
        