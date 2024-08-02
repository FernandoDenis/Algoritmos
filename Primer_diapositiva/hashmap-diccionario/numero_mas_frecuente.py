
#Encontrar el numero mas frequente en un array.

array = [ 4,  9,  4,  3,  8,  8, 10,  2,  1,  9,  3,  5,  2,  9,  6,  4,  4,
        2,  4,  4,  4, 10,  5,  8,  8,  4,  2,  9,  6,  4,  1,  3,  8,  2,
        9,  7,  1,  7,  1,  5,  4,  5,  4,  3,  2,  2,  2,  5,  8,  2,  9,
       10,  3,  5, 10,  3,  2,  8,  2,  4, 10,  1,  6,  4,  2,  5,  9,  4,
        9, 10,  5,  1,  8,  3,  1,  1,  1,  6, 10,  4, 10,  6,  2,  8,  6,
        9,  9,  1,  7,  4,  9,  1,  2,  9,  5, 10,  3,  1, 10,  8]

diccionario = {}

for i in array:
    if(i in diccionario):
        diccionario[i] += 1
    else:
        diccionario[i] = 1
        
numerMayor = 0
valor = 0

for keys,value in diccionario.items():
    if(value > numerMayor):
        numerMayor = value
        valor = keys
        
print(f"El numero mas frecuente en un array es {valor}")
    