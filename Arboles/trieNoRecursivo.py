
class Node:
    def __init__(self, letra, accion = None):
        self.childs = dict() 
        self.letra = letra
        self.accion = accion 

class Trie:
    def __init__(self):
        self.root = Node("", None)

    def agregar(self, palabra, accion):
        letra = 0
        nodoActual = self.root

        while letra < len(palabra) and palabra[letra] in nodoActual.childs:
            nodoActual = nodoActual.childs[palabra[letra]]
            letra += 1

        while letra < len(palabra):
            nuevoNodo = Node(palabra[letra])
            nodoActual.childs[palabra[letra]] = nuevoNodo
            nodoActual = nuevoNodo
            letra += 1

        nodoActual.accion = accion

    def completar(self, palabra):
        listado = []
        idxLetra = 0
        nodoActual = self.root

        while idxLetra < len(palabra) and palabra[idxLetra] in nodoActual.childs:
            nodoActual = nodoActual.childs[palabra[idxLetra]]
            idxLetra += 1

        self._completar(nodoActual,palabra[: -1], listado)
        return listado
    
    def _completar(self, node, prefijo, lista):
        letraActual = node.letra
        palabra = prefijo
        palabra += letraActual

        if node.accion != None:
            lista.append({palabra, node.accion})

        for node, child in node.childs.items():
            self._completar(child, palabra, lista)

trieTry = Trie()

palabra = "hola como estan"

for i in range(len(palabra)):
    trieTry.agregar(palabra[i:] ,i)

completado = trieTry.completar("como")

print(completado)


# print(trieTry.root.childs['H'].__dict__)

"""
'Hilo', 'JUAS'

5 < 0
H : 

letra = 0
nodoActual = {}

"""
