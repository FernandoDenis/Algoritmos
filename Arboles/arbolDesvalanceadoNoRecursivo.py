class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.visited = False

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

    def search(self, data):
        nextNode = self.root
        while(nextNode != None):
            if(data == nextNode.data):
                return True  
            elif(data < nextNode.data):
                nextNode = nextNode.left
            else:
                nextNode = nextNode.right
        return False  
    
    def print(self):
        pila = []
        pila.append(self.root)
        while(len(pila) > 0):
            node = pila.pop()
            if node is not None and not node.visited:
                print(node.data)
                node.visited = True
                pila.append(node.left)
                pila.append(node.right)

    def orderPrint(self):
        pila = []
        pila.append(self.root)
        while(len(pila)):
            node = pila.pop()
            if node.left is not None:
                if not node.left.visited:
                    pila.append(node)
                    pila.append(node.left)
                    continue
                else:
                    print(node.data)
                    node.visited = True
            else:
                print(node.data)
                node.visited = True

            if node.visited and node.right is not None:
                if not node.right.visited:
                    pila.append(node.right)
                
                
# 3, 7


miArbol = BinaryTree()
miArbol.insert(5)
miArbol.insert(3)
miArbol.insert(2)
miArbol.insert(1)
miArbol.insert(4)
miArbol.insert(6)
miArbol.insert(7)

print(miArbol.search(4))  
print(miArbol.search(10)) 

miArbol.orderPrint()
