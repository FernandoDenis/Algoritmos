class Node:
    def __init__(self, letra, accion):
        self.childs = dict() 
        self.letra = letra
        self.accion = accion 

class Trie:
    def __init__(self):
        self.root = Node("", None)

    def agregar(self, palabra, accion):
        self._agregar(self.root, palabra, accion, 0)

    def _agregar(self, node, palabra, accion, contador):
        if contador == len(palabra):
            node.accion = accion
            return

        if palabra[contador] not in node.childs:
            node.childs[palabra[contador]] = Node(palabra[contador], None)

        self._agregar(node.childs[palabra[contador]], palabra, accion, contador + 1)

trieTry = Trie()

trieTry.agregar("Hola", "JEJEJE")
trieTry.agregar("Hilo", "JUAS")

print(trieTry.root.__dict__)