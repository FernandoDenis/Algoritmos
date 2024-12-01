from b_tree import BTree, BTreeNode

# Pruebas con pytest
import pytest
import random

def test_btree_large_random_insert():
    # Crear un B-tree de orden t = 3
    btree = BTree(3)

    # Generar 3000 claves aleatorias únicas en el rango [1, 10000]
    keys_to_insert = random.sample(range(1, 10001), 3000)

    # Insertar las claves en el B-tree
    for key in keys_to_insert:
        btree.insert(key)

    # Probar que todas las claves insertadas existen en el B-tree
    for key in keys_to_insert:
        result = btree.search(key)
        assert result is not None, f"La clave {key} debería existir en el B-tree"
        assert result[0].keys[result[1]] == key, f"La clave {key} no fue encontrada correctamente en el B-tree"

    # Probar que algunas claves no insertadas no existen en el B-tree
    non_existent_keys = random.sample([key for key in range(1, 10001) if key not in keys_to_insert], 10)
    for key in non_existent_keys:
        result = btree.search(key)
        assert result is None, f"La clave {key} no debería existir en el B-tree"

if __name__ == "__main__":
    # Ejecutar la prueba
    test_btree_large_random_insert()
    print("Prueba de 3000 elementos aleatorios pasada correctamente.")
