class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.childs = []

class BTree:
    def __init__(self, degree):
        self.root = BTreeNode(True)
        self.degree = degree

    def insert(self, value):
        root = self.root
        if len(root.keys) == (2 * self.degree) - 1:
            # La raíz está llena, crear una nueva raíz y dividir
            new_root = BTreeNode(False)
            # new_root es el nuevo nodo padre e inserta en sus hijos el nodo que estaba lleno
            new_root.childs.insert(0, root)
            # Divide en 2 el nodo lleno y lo pone de hijos de new_root
            self._split_child(new_root, 0)
            # Ahora que los nodos ya no están llenos llama a la función para que los inserte
            self._insert_nonfull(new_root, value)
            self.root = new_root
        else:
            self._insert_nonfull(root, value)

    def _split_child(self, parent, i):
        degree = self.degree
        # Guarda la variable de root hijo para dividirlo (El hijo es el nodo que estaba lleno)
        node_to_split = parent.childs[i]
        # Crea un nuevo nodo que será el nodo hijo que tendrá la otra mitad del nodo lleno
        new_node = BTreeNode(node_to_split.leaf)

        # Mover la clave mediana al nodo padre
        parent.keys.insert(i, node_to_split.keys[degree - 1])
        # Se agrega como hijos el otro nodo que contendrá la otra mitad de los valores
        parent.childs.insert(i + 1, new_node)

        # Dividir las claves entre el nodo original y el nuevo nodo
        new_node.keys = node_to_split.keys[degree:(2 * degree) - 1]
        node_to_split.keys = node_to_split.keys[0:degree - 1]

        # Dividir los hijos si no es una hoja
        if not node_to_split.leaf:
            new_node.childs = node_to_split.childs[degree:(2 * degree)]
            node_to_split.childs = node_to_split.childs[0:degree]

    def _insert_nonfull(self, node, value):
        i = len(node.keys) - 1
        if node.leaf:
            # Insertar la nueva clave en la posición correcta
            node.keys.append(None)
            while i >= 0 and value < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = value
        else:
            # Encontrar el hijo al que se debe hacer la recursión
            while i >= 0 and value < node.keys[i]:
                i -= 1
            i += 1
            # Busca el índice del hijo al que pertenece el valor a insertar y llama de nuevo la función
            if len(node.childs[i].keys) == (2 * self.degree) - 1:
                # Si el hijo está lleno, dividirlo
                self._split_child(node, i)
                # Después de dividir, determinar en cuál de los dos nodos insertar
                if value > node.keys[i]:
                    i += 1
            # Llamada recursiva para insertar en el hijo adecuado
            self._insert_nonfull(node.childs[i], value)

    def search(self, k, node=None, nivel = 0):
        print(str(nivel) + " nivel")
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and k == node.keys[i]:
            return node, i
        elif node.leaf:
            return None
        else:
            return self.search(k, node.childs[i], nivel + 1)
        
btree = BTree(3)

for i in range(1,18):
    btree.insert(i)
