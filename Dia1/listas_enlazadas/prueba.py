
#Lista simple para insertar valores al final, insertar despues de un valor conocido (y si el valor no existe insertarlo al final), eliminar cualquier valor que busque 

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
        
    def insertAfterData(self,limit,data):
        if (self.head == None):
            self.head = Node(data)
            return
        actualNode = self.head
        while(actualNode.next != None):
            if(actualNode.data != limit):
                actualNode = actualNode.next
            else:
                tempNext = actualNode.next
                actualNode.next = Node(data)
                actualNode.next.next = tempNext
                return
        self.insertAtEnd(data)
        
    def removeAny(self,dataToRemove):
        nodoActual = self.head
        if(nodoActual.data == dataToRemove):
            self.head = nodoActual.next
            return
        while (nodoActual.next != None):
            if (nodoActual.next.data != dataToRemove):
                nodoActual = nodoActual.next
            else:
                nodoActual.next = nodoActual.next.next
                return
        
    def printList(self):
        if (self.head == None):
            print(None)
        completeList = ""
        actualNode = self.head
        while (actualNode != None):
            completeList += f"{actualNode.data} -> "
            actualNode = actualNode.next
        print(completeList)
        
lista_enlazada = LinkedList()

lista_enlazada.insertAtEnd(1)
lista_enlazada.insertAtEnd(1)
lista_enlazada.insertAtEnd(2)
lista_enlazada.insertAtEnd(4)
lista_enlazada.insertAtEnd(5)

lista_enlazada.printList() 
print("\n")

lista_enlazada.insertAfterData(2,3)
lista_enlazada.insertAfterData(1,0.5)
lista_enlazada.insertAfterData(10,6)

lista_enlazada.printList()
print("\n")

lista_enlazada.removeAny(2)

lista_enlazada.printList()
print("\n")