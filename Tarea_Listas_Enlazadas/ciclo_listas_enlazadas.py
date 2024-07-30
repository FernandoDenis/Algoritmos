class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtEnd(self,data):
        if (self.head == None): 
            self.head = Node(data)
            return 
        actualNode = self.head
        while (actualNode.next != None):
            actualNode = actualNode.next
        actualNode.next = Node(data)
        
    def generateCycle(self):
        nodoActual = self.head
        contador = 0
        while(nodoActual.next != None):
            contador += 1
            nodoActual = nodoActual.next
        ultimoNodo = nodoActual
        contador2 = 0
        nodoActual = self.head
        while(contador2 != contador - 3):
            contador2 += 1
            nodoActual = nodoActual.next
        ultimoNodo.next = nodoActual
        return 
        
    def breakCycle(self):
        nodoActual = self.head
        noCycle = set()
        while(nodoActual != None):
            if not(nodoActual.next in noCycle):
                noCycle.add(nodoActual)
            else:
                nodoActual.next = None
            nodoActual = nodoActual.next
    
    def printList(self):
        if (self.head == None):
            print(None)
        completeList = ""
        actualNode = self.head
        while (actualNode != None):
            completeList += f"{actualNode.data} -> "
            actualNode = actualNode.next
        print(completeList)
        
lista = LinkedList()
lista.insertAtEnd(1)
lista.insertAtEnd(2)
lista.insertAtEnd(3)
lista.insertAtEnd(4)
lista.insertAtEnd(5)
print(lista.generateCycle())
print(lista.breakCycle())
lista.printList()
