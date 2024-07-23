#Eliminar duplicados

import random

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self,data):
        if (self.head == None):
            self.head = Node(data)
            return 
        else:
            self.head, self.head.next = Node(data), self.head
    
    def insertAtEnd(self,data):
        nodo_actual = self.head
        if (self.head == None): 
            self.head = Node(data)
            return 
        else:
            while nodo_actual.next != None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = Node(data)
    
    def printList(self):
        nodo_actual = self.head
        nodo = ""
        while (nodo_actual != None):
            nodo += f"{nodo_actual.data} -> "
            nodo_actual = nodo_actual.next
        return nodo
    
    def eliminatedDuplicates(self):
        if (self.head == None): return
        nodo_actual = self.head
        while (nodo_actual.next != None):
            siguiente_nodo = nodo_actual.next
            while (siguiente_nodo.next != None):
                if (nodo_actual.data == siguiente_nodo.next.data):
                    siguiente_nodo.next = siguiente_nodo.next.next
                else:
                    siguiente_nodo = siguiente_nodo.next
            nodo_actual = nodo_actual.next
    
lista_enlazada = LinkedList()

for i in range(1000):
    lista_enlazada.insertAtBeginning(random.randint(1,500))

print(lista_enlazada.printList())
lista_enlazada.eliminatedDuplicates()
print("\n\n\n")
print(lista_enlazada.printList())
