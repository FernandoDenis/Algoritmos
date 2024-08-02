
#Dada una lista de numeros identificar los numeros repetidos
array = [4, 9, 4, 3, 8, 7, 10, 2, 1, 9, 3, 5, 2, 9, 6, 4, 4, 2, 4, 4, 4, 10, 5, 8, 6, 4, 2, 9, 6, 4, 1, 3, 8, 2, 9, 1, 5, 4, 5, 4, 3, 2, 2, 2, 5, 8, 2, 9, 10, 3, 5, 10, 3, 2, 8, 2, 4, 10, 1, 6, 4, 2, 5, 9, 4, 9, 10, 5, 1, 8, 3, 1, 1, 1, 6, 10, 4, 10, 6, 2, 8, 6, 9, 9, 1, 4, 9, 1, 2, 9, 5, 10, 3, 1, 10, 8]

numerosSinRepetir = set()
numerosRepetidos = set()
for i in array:
    if not(i in numerosSinRepetir):
        numerosSinRepetir.add(i)
    else:
        numerosRepetidos.add(i)
        
print(numerosRepetidos)