# black and red tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if(self.root == None):
            self.root = Node(data)
            return
        else:
            nextNode = self.root
            while(nextNode != None):
                if(data < nextNode.data):
                    if(nextNode.left == None):
                        nextNode.left = Node(data)
                        return
                    else:
                        nextNode = nextNode.left
                else:
                    if(nextNode.right == None):
                        nextNode.right = Node(data)
                        return
                    else:
                        nextNode = nextNode.right

    def delete(self, data):
        node = self.root
        padre = None

        # El nodo no sea none y el dato sea distinto al valor buscado
        while (node and node.data != data):
            padre = node
            if data < node.data:
                node = node.left
            else:
                node = node.right

        # No esta en el arbol
        if (node == None):
            return
        
        if (node.left == None and node.right == None):
            if node != self.root:
                if padre.left == node:
                    padre.left = None
                else:
                    padre.right = None
            else:
                self.root = None

