
class Node: 
    def __init__(self,id,edad,dinero,nombre):
        self.id = int(id)
        self.edad = int(edad)
        self.dinero = int(dinero)
        self.nombre = str(nombre)
        self.next = None
        self.back = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def agregarAlInicio(self,id,edad,dinero,nombre):
        self.head,self.head.next = Node(id,edad,dinero,nombre),self.head
        self.head.next.back = self.head
        
    def agregarAlFinal(self,id,edad,dinero,nombre):
        if(self.head == None):
            self.head = Node(id,edad,dinero,nombre)
            return
        else:
            nodoActual = self.head
            while (nodoActual.next != None):
                nodoActual = nodoActual.next
            nodoActual.next = Node(id,edad,dinero,nombre)
            nodoActual.next.back = nodoActual
            return
        
    def eliminarAlInicio(self):
        NodoBorrado = self.head
        self.head = self.head.next
        self.head.back = None
        return NodoBorrado
    
    def eliminarAlFinal(self): #Problema cuando queda 1 elemento
        nodoActual = self.head
        while(nodoActual.next.next != None):
            nodoActual = nodoActual.next
        
        NodoBorrado = nodoActual.next
        nodoActual.next.back = None
        nodoActual.next = None
        return NodoBorrado
        
    def eliminar(self,id):
        if(id < 0):
            return False
        if(self.head.id == id):
            NodoBorrado = self.head
            self.head = self.head.next
            self.head.back = None
            return NodoBorrado
        nodoActual = self.head
        while (nodoActual.next.id != id):
            nodoActual = nodoActual.next
            if(nodoActual.next == None):
                return False
            
        if(nodoActual.next.next != None):
            NodoBorrado = nodoActual.next
            nodoActual.next = nodoActual.next.next 
            nodoActual.next.back = nodoActual
            return NodoBorrado
        else:
            NodoBorrado = nodoActual.next
            nodoActual.next = nodoActual.next.next 
            return NodoBorrado
        
    def buscarElemento(self,id):
        if(id < 0):
            return False
        nodoActual = self.head
        while(nodoActual.id != id):
            if(nodoActual.next != None):
                nodoActual = nodoActual.next
            elif(nodoActual.next == None):
                return False
            elif(nodoActual.next.id == id):
                return nodoActual.next
            else:
                return False
        return nodoActual
        
        
    def print(self):
        nodoActual = self.head
        while (nodoActual != None):
            print(nodoActual.id, end=" -> ")
            nodoActual = nodoActual.next
        return
    
lista = LinkedList()

lista.agregarAlFinal(1,23,1000,"Julieta")
lista.agregarAlFinal(2,20,500,"Fernando")
lista.agregarAlFinal(3,22,40,"Pablo")
lista.agregarAlFinal(4,11,20000,"Toby")
lista.agregarAlInicio(0,21,300,"Diego")
print(lista.eliminarAlInicio())

lista.print()

            