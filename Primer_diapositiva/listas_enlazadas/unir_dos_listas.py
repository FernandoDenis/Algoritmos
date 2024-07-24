
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
        
    def insetBeforeData (self,limit,data):
        if(self.head == None):
            self.head = Node(data)
            return
        elif (limit == self.head.data):
            nextNode = self.head
            self.head = Node(data)
            self.head.next = nextNode
            return
        actualNode = self.head
        while (actualNode.next != None):
            if (actualNode.next.data != limit):
                actualNode = actualNode.next
            else:
                tempNext = actualNode.next
                actualNode.next = Node(data)
                actualNode.next.next = tempNext
                return
        self.insertAtEnd(data)
                         
    def joinList(self,otherList):
        actualNode = self.head
        otherNode = otherList.head
    
        while (otherNode != None):
            # ANTES AQUI IBA
            while (actualNode != None):
                if(actualNode == otherNode):
                    self.insertAfterData(actualNode.data,otherNode.data)
                    break
                elif(actualNode.data > otherNode.data):
                    self.insetBeforeData(actualNode.data,otherNode.data)
                    break
                elif(actualNode.next == None):
                    self.insertAtEnd(otherNode.data)
                    break
                elif(actualNode.data < otherNode.data):
                    actualNode = actualNode.next
                    
            actualNode = self.head #AHORA VA AQUI Y SE MODIFICIO DE OTHERNODE.NEXT A SELF.HEAD
            otherNode = otherNode.next
        
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
lista_enlazada.insertAtEnd(2)
lista_enlazada.insertAtEnd(3)
lista_enlazada.insertAtEnd(4)
lista_enlazada.insertAtEnd(10)

lista_enlazada.printList()
print("\n")

lista_enlazada2 = LinkedList()

lista_enlazada2.insertAtEnd(4.5)
lista_enlazada2.insertAtEnd(5)
lista_enlazada2.insertAtEnd(6)
lista_enlazada2.insertAtEnd(7)
lista_enlazada2.insertAtEnd(8)

lista_enlazada2.printList()
print("\n")

lista_enlazada.joinList(lista_enlazada2)
lista_enlazada.printList()
