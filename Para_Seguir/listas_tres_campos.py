
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
        
    def agregar(self,id,edad,dinero,nombre):
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
        
    def eliminar(self,id):
        if(self.head.id == id):
            self.head = self.head.next
            self.head.back = None
            return
        nodoActual = self.head
        while (nodoActual.next.id != id):
            nodoActual = nodoActual.next
        if(nodoActual.next.next != None):
            nodoActual.next = nodoActual.next.next 
            nodoActual.next.back = nodoActual
            return
        else:
            nodoActual.next = nodoActual.next.next 
            return
        
    def buscarElemento(self,id):
        if(id <= 0):
            return f"El ID:{id} no existe"
        nodoActual = self.head
        while(nodoActual.id != id):
            if(nodoActual.next != None):
                nodoActual = nodoActual.next
            elif(nodoActual.next.id == id):
                return F"ID:{nodoActual.next.id}\nNombre:{nodoActual.next.nombre}\nDinero:${nodoActual.next.dinero}\nEdad:{nodoActual.next.edad}"
            else:
                return f"El ID:{id} no existe"
        return F"ID:{nodoActual.id}\nNombre:{nodoActual.nombre}\nDinero:${nodoActual.dinero}\nEdad:{nodoActual.edad}\n"
        
        
    def print(self):
        nodoActual = self.head
        while (nodoActual != None):
            print(nodoActual.id, end=" -> ")
            nodoActual = nodoActual.next
        return
    
# lista = LinkedList()

# lista.agregar(1,23,1000,"Julieta")
# lista.agregar(2,20,500,"Fernando")
# lista.agregar(3,22,40,"Pablo")
# lista.agregar(4,11,20000,"Toby")
# print(lista.buscarElemento(1))
# lista.print()

            