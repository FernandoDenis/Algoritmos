class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.recursiveInsert(data, self.root)

    def recursiveInsert(self, data, node):
        currentNode = node
        if data < currentNode.data:
            if currentNode.left is None:
                currentNode.left = Node(data)
            else:
                self.recursiveInsert(data, currentNode.left)
        else:
            if currentNode.right is None:
                currentNode.right = Node(data)
            else:
                self.recursiveInsert(data, currentNode.right)

    def recursiveSearch(self, data, node):
        if node is None:
            return False  
        if data == node.data:
            return True 
        elif data < node.data:
            return self.recursiveSearch(data, node.left)
        else:
            return self.recursiveSearch(data, node.right)
        
    def print(self):
        self._print(self.root)

    def _print(self, node):
        if(node == None):
            return
        print(node.data)
        self._print(node.left)
        self._print(node.right)



# Ejemplo de uso:
miArbol = BinaryTree()
miArbol.insert(5)
miArbol.insert(3)
miArbol.insert(2)
miArbol.insert(1)
miArbol.insert(4)
miArbol.insert(6)
miArbol.insert(7)

print(miArbol.recursiveSearch(4, miArbol.root)) 
print(miArbol.recursiveSearch(10, miArbol.root)) 

miArbol.print()
