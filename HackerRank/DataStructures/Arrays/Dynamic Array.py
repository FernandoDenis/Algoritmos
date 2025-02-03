# 2.0 Flash Experimental. Might not work as expected.
# Entendido. Aquí está la descripción del problema "Dynamic Array" transcrita directamente de la imagen, en su idioma original (inglés):

# Problem Description "Dynamic Array"

# Declare a 2-dimensional array, arr, of n empty arrays. All arrays are zero indexed.

# Declare an integer, lastAnswer, and initialize it to 0.   

# There are 2 types of queries, given as an array of strings for you to parse:

# Query: 1 x y

# Let idx = ((x ^ lastAnswer) % n).
# Append the integer y to arr[idx].
# Query: 2 x y

# Let idx = ((x ^ lastAnswer) % n).
# Assign the value arr[idx][y % size(arr[idx])] to lastAnswer.
# Store the new value of lastAnswer to an answers array.   
# Note: ^ is the bitwise XOR operation, which corresponds to the ^ operator in most languages. % is the modulo operator. Finally, size(arr[idx]) is the number of elements in arr[idx].

# Function Description

# Complete the dynamicArray function below.   

# dynamicArray has the following parameters:

# int n: the number of empty arrays to initialize in arr   
# string queries[q]: query strings that contain 3 space-separated integers
# Returns

# int[]: the results of each type 2 query in the order they are presented
# Input Format

# The first line contains two space-separated integers, n, the size of arr to create, and q, the number of queries, respectively.   

# Each of the q subsequent lines contains a query string, queries[i].   

# Constraints

# 1 ≤ n, q ≤ 10<sup>5</sup>
# 0 ≤ x, y ≤ 10<sup>9</sup>
# It is guaranteed that type 2 query will never query an empty array or index.   


def dynamicArray(n, queries):
    array = [[] for _ in range(n)] # Aqui no srive hace el ([[]] * n) ya que crea dos arrays que son iguales por lo que al agregar un valor dentro de ese array se va a agregar en el otro
    result = []
    lastAnswer = 0

    for i in queries:
        if i[0] == 1:
            idx = (i[1] ^ lastAnswer) % n
            array[idx].append(i[2])
        else:
            idx = (i[1] ^ lastAnswer) % n
            lastAnswer = array[idx][i[2] % len(array[idx])]
            result.append(lastAnswer)
            
    return array

print(dynamicArray(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]))

