import pytest
from bloomFilter import BloomFilter

def test_small():
    # Crear un filtro con tamaño pequeño y pocas funciones hash
    bf = BloomFilter(50, 3)

    elements = ["apple", "banana", "cherry"]
    for element in elements:
        bf.add(element)

    for element in elements:
        assert bf.contains(element), f"{element} debería estar en el filtro."

    # Comprobar un elemento no añadido, permitiendo falsos positivos
    unadded_element = "grape"
    contains_unadded = bf.contains(unadded_element)
    assert isinstance(contains_unadded, bool), "La respuesta debe ser booleana."

def test_big():
    # Crear un filtro con tamaño grande y más funciones hash
    bf = BloomFilter(1000000, 5)

    elements = [f"item_{i}" for i in range(10000)]
    for element in elements:
        bf.add(element)

    for element in elements:
        assert bf.contains(element), f"{element} debería estar en el filtro."

    false_positives = 0
    test_elements = [f"test_{i}" for i in range(10000, 20000)]
    for element in test_elements:
        if bf.contains(element):
            false_positives += 1

    assert false_positives / len(test_elements) < 0.10, "La tasa de falsos positivos es demasiado alta." # Si la tasa es demasiado alta aumentar la memoria

def test_edge_cases():
    # Crear un filtro con tamaño mínimo
    bf = BloomFilter(10, 1)

    bf.add("test")
    assert bf.contains("test"), "'test' debería estar en el filtro."
    
    # Probar un elemento que no debería estar, permitiendo falsos positivos
    unadded_element = "otro"
    contains_unadded = bf.contains(unadded_element)
    assert isinstance(contains_unadded, bool), "La respuesta debe ser booleana."

    # Probar con un filtro vacío
    bf_empty = BloomFilter(100, 3)
    empty_element = "nada"
    assert not bf_empty.contains(empty_element), f"'{empty_element}' no debería estar en el filtro vacío"

def test_medium_dataset():
    """
    Prueba con un conjunto de datos mediano para evaluar el comportamiento del filtro.
    """
    
    bf = BloomFilter(1000000, 5)

    # Generar un conjunto de datos de tamaño medio
    elements = [f"item_{i}" for i in range(300000)]  # 300,000 elementos
    unadded_elements = [f"test_{i}" for i in range(300000, 600000)]

    # Agregar los elementos al filtro
    for element in elements:
        bf.add(element)

    # Verificar que los elementos añadidos estén presentes
    for element in elements:
        assert bf.contains(element), f"{element} debería estar en el filtro."

    # Verificar falsos positivos
    for element in unadded_elements:
        assert isinstance(bf.contains(element), bool), f"'{element}' debería retornar un valor booleano."

def test_edge_cases_medium():
    """
    Prueba con casos extremos, como filtro lleno o cerca de su límite, con un tamaño medio.
    """
    
    bf = BloomFilter(500000, 4)

    # Llenar el filtro con un conjunto de datos mediano
    elements = [f"edge_{i}" for i in range(500000 // 20)] 
    for element in elements:
        bf.add(element)

    # Verificar que los elementos añadidos estén presentes
    for element in elements:
        assert bf.contains(element), f"{element} debería estar en el filtro."

    # Probar un elemento no añadido
    unadded_element = "unadded_item"
    assert isinstance(bf.contains(unadded_element), bool), "La respuesta debe ser booleana."
