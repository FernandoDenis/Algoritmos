# There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

def hourglassSum(arr):
    countX = 0
    countY = 0
    suma = 0
    sumaMayor = -64 # -64 es el numero menor que no alcanza la suma de todos los numeros menores de hourglass (-9 x 7) = -63
    
    for i in range(0,16): # Canttidad de numeros que es necesario pasar
    
        if i % 4 == 0 and i != 0: # Condicion para saber cuando pasar a otra fila
            countY += 1
            countX = 0
        
        # Es la suma de cada elemento en el hourglass
        suma = arr[0 + countY][0 + countX] + arr[0 + countY][1 + countX] + arr[0 + countY][2 + countX] + arr[1 + countY][1 + countX] + arr[2 + countY][0 + countX] + arr[2 + countY][1 + countX] + arr[2 + countY][2 + countX]
        
        # Encontrar el numero mayor
        if suma > sumaMayor:
            sumaMayor = suma
        
        countX += 1
        
    return sumaMayor

array_2d = [
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -2, -3, -4, -5],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5]
]


print(hourglassSum(array_2d))