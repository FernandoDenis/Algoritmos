from cache_LRU import LRUCache

import pytest, time

def test_basic():
    cache = LRUCache(7)
    cache.put(1, "A")
    assert cache.get(1) == "A"
    assert cache.get(2) == -1
    
def test_medium():
    cache = LRUCache(7)
    cache.put(1, "A")
    time.sleep(0.1)
    cache.put(2, "B")
    time.sleep(0.1)
    cache.put(3, "C")
    time.sleep(0.1)
    cache.put(4, "D")
    time.sleep(0.1)
    cache.put(5, "F")
    time.sleep(0.1)
    cache.put(6, "G")
    time.sleep(0.1)
    cache.put(7, "I")
    time.sleep(0.1)
    cache.put(8, "J")
    assert cache.get(1) == -1 # Al agregarse un 8tavo elemento el elemento mas viejo en este caso el 1 deberia haber sido borrado

def test_lru_update():
    cache = LRUCache(7)
    cache.put(1, "A")
    cache.put(2, "B")
    cache.get(1)  # Accede al elemento para hacerlo más reciente
    cache.put(3, "C")  
    cache.put(4, "D") 
    cache.put(5, "E")  
    cache.put(6, "F")  
    cache.put(7, "G")  
    cache.put(8, "H") 
    assert cache.get(2) == -1  # El elemento 2 debe haberse eliminado
    
def test_hard():
    cache = LRUCache(7)
    assert cache.get(1) == -1 # Prueba de error cuando no hay ningun elemento
    
    cache.put(1, "A")
    time.sleep(0.1)
    
    cache.put(2, "B")
    time.sleep(0.1)
    
    cache.put(3, "C")  
    time.sleep(0.1)
    
    cache.put(4, "D") 
    time.sleep(0.1)
    
    cache.put(5, "E")  
    time.sleep(0.1)
    
    cache.put(6, "F") 
    time.sleep(0.1)
     
    cache.put(7, "G")  # mas reciente
    time.sleep(0.1)
    
    cache.get(1)
    cache.get(2)
    cache.get(3)  
    cache.get(4) 
    cache.get(5)  
    cache.get(6)  
    print(cache.memory)
    
    cache.put(8, "H")
    assert cache.get(7) == -1 # Despues de actualizar todos antes del mas reciente, el mas reciente debe convertirse en el mas viejo
    
def test_limit():
    cache = LRUCache(7)
    for i in range(7):
        cache.put(i, f"Item{i}")
    assert len(cache.memory) == 7  # Verifica que no haya excedido el límite