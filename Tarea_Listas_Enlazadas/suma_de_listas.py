
class Node: 
    def __init__(self,numero):
        self.numero = int(numero)
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def agregarAlInicio(self,numero):
        self.head,self.head.next = Node(numero),self.head
        
    def agregarAlFinal(self,numero):
        if(self.head == None):
            self.head = Node(numero)
            return
        else:
            nodoActual = self.head
            while (nodoActual.next != None):
                nodoActual = nodoActual.next
            nodoActual.next = Node(numero)
            return
        
    def eliminarAlInicio(self):
        NodoBorrado = self.head
        self.head = self.head.next
        return NodoBorrado
    
    def eliminarAlFinal(self):
        if(self.head == None):
            return 0
        elif(self.head.next == None):
            NodoBorrado = self.head
            self.head = None
            return NodoBorrado
        nodoActual = self.head
        while(nodoActual.next.next != None):
            nodoActual = nodoActual.next
        
        NodoBorrado = nodoActual.next
        nodoActual.next = None
        return NodoBorrado
        
    def print(self):
        nodoActual = self.head
        while (nodoActual != None):
            print(nodoActual.numero, end=" -> ")
            nodoActual = nodoActual.next
        return
    
    def length(self):
        nodoActual = self.head
        contador = 0
        while(nodoActual != None):
            contador += 1
            nodoActual = nodoActual.next
        return contador

def sumarDosListas(lista1,lista2):
    suma = LinkedList()
    if(lista1.length() >= lista2.length()):
        max = lista1.length()
    else:
        max = lista1.length()
    carry = 0
    while(max != 0):
        resultado = lista1.eliminarAlFinal().numero + lista2.eliminarAlFinal().numero + carry
        carry = 0
        if(resultado > 9):
            carreoAnterior = resultado // 10
            carry += carreoAnterior
            resultado -= carreoAnterior * 10
            suma.agregarAlInicio(resultado)
        else:
            suma.agregarAlInicio(resultado)
            carry = 0
        max -= 1
        
    if(carry > 0):
        suma.agregarAlInicio(carry)
    return suma

lista = LinkedList()
lista.agregarAlFinal(6)
lista.agregarAlFinal(5)
lista.agregarAlFinal(6)
lista.agregarAlFinal(5)
lista.agregarAlFinal(6)
lista.agregarAlFinal(5)
lista.agregarAlFinal(6)
lista.agregarAlFinal(5)

lista2 = LinkedList()
lista2.agregarAlFinal(4)
lista2.agregarAlFinal(5)
lista2.agregarAlFinal(4)
lista2.agregarAlFinal(5)
lista2.agregarAlFinal(4)
lista2.agregarAlFinal(5)
lista2.agregarAlFinal(4)
lista2.agregarAlFinal(5)

sumarDosListas(lista,lista2).print()

