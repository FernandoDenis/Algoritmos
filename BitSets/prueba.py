
from usandoBitsets import BitVector

prueba = BitVector(4300000000)

print("Empieza")

with open('BitSets/output.txt', 'r') as archivo:
    for linea in archivo:
        numero = linea.strip()
        numero = int(numero)
        prueba.set(numero)

    print(bin(prueba.vector[0]))
    print(prueba.foundUnique())