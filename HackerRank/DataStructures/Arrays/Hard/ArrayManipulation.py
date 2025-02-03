
# Descripción del Problema:
# Dado un arreglo de ceros con índices basados en 1 (1-indexado) y una lista de operaciones, 
# para cada operación debes agregar un valor a todos los elementos del arreglo entre dos índices dados, inclusivos. 
# Una vez completadas todas las operaciones, devuelve el valor máximo en el arreglo resultante.

# Ejemplo:

# Entrada:
# n = 10 (tamaño del arreglo)
# queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

# Cada consulta se interpreta como:
# a   b   k
# 1   5   3
# 4   8   7
# 6   9   1

# Operaciones:
# Para cada consulta (a, b, k), se suma k a todos los elementos del arreglo entre a y b (ambos inclusivos):

# 1. Después de la primera operación [1, 5, 3]:
#    [3, 3, 3, 3, 3, 0, 0, 0, 0, 0]

# 2. Después de la segunda operación [4, 8, 7]:
#    [3, 3, 3, 10, 10, 7, 7, 7, 0, 0]

# 3. Después de la tercera operación [6, 9, 1]:
#    [3, 3, 3, 10, 10, 8, 8, 8, 1, 0]

# El valor máximo después de todas las operaciones es 10.

# Función a implementar:
# arrayManipulation

# Parámetros:
# 1. int n: El tamaño del arreglo.
# 2. list queries[q][3]: Una lista bidimensional donde cada elemento es una consulta con tres enteros (a, b, k).

# Retorno:
# int: El valor máximo en el arreglo resultante.

# Formato de Entrada:
# 1. La primera línea contiene dos enteros separados por espacio, n y m, 
#    que representan el tamaño del arreglo y el número de operaciones, respectivamente.
# 2. Las siguientes m líneas contienen tres enteros separados por espacio: a, b y k, los índices del rango y el valor a sumar.

# Restricciones:
# - 3 <= n <= 10^7
# - 1 <= m <= 2 * 10^5
# - 1 <= a <= b <= n
# - 0 <= k <= 10^9

# Este problema yo no lo pude resolver, pero esta es la solucion que le entendi

def arrayManipulation(n, queries):
    arr = [0] * n # Tamaño del array
    
    for i in queries:
        arr[i[0] - 1] += i[2] # Marca el inicio de las posiciones donde ira el valor en esa misma posicion
        
         # Condicion para agregar el fin del limite de la posicion
         # Pero si el fin es igual a la longitud del array NO es necesario poner fin ya que todos los numeros son afectados por ese valor
        if i[1] != len(arr):
            arr[i[1]] -= i[2] # Se resta el valor al indice en donde ya ha terminado para que no afecte a los demas
            
    valorMasGrande = 0
    sumaDeValores = 0
    print(arr)
    
    for i in arr:
        sumaDeValores += i
        if sumaDeValores > valorMasGrande:
            valorMasGrande = sumaDeValores
            
    return valorMasGrande

print(arrayManipulation(5,[[1,2,100],[2,5,100],[3,4,100]]))

