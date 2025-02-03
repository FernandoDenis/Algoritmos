# A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. Given an integer, d, rotate the array that many steps left and return the result.

# Example
# d = 2
# arr = [1, 2, 3, 4, 5]
# After 2 rotations, arr' = [3, 4, 5, 1, 2].

# Function Description
# Complete the rotateLeft function in the editor below.

# rotateLeft has the following parameters:

# int d: the amount to rotate by
# int arr[n]: the array to rotate
# Returns

# int[n]: the rotated array
# Input Format
# The first line contains two space-separated integers that denote n, the number of integers, and d, the number of left rotations to perform.
# The second line contains n space-separated integers that describe arr[].

# Constraints

# 1 ≤ n ≤ 10⁵
# 1 ≤ d ≤ n
# 1 ≤ a[i] ≤ 10⁶

# MI RESPUESTA:

def rotateLeft(d, arr):
    newArr = []
    # El ciclo lo agrega en otro array ya ordenando haciendo que el elemento agregado sea el que este n eleemntos adelante
    # Ejemplo, si d es 2, entonces empezara en en la posicion -3 que es equivalente a la posicion 2 si el array fuera este: [1,2,3,4,5]
    # Lo trabajo con numeros negativos porque de esa forma puede darle la vuelta al array en usando un solo for.
    for i in range(d - len(arr),(d - len(arr)) + len(arr)): 
        newArr.append(arr[i])
        
    return newArr

# Respuesta mas rapida

def optimized_rotateLeft(d, arr):
    return arr[d % len(arr):] + arr[:d % len(arr)]