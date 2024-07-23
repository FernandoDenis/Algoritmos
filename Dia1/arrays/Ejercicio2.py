
a = [1,2,5]
b = [0,3,7,4]

def insertar_valor(array, valor, indice):
    array.append(None)
    for i in range(len(array) - 1,indice,-1):
        array[i] = array[i - 1]
    array[indice] = valor
    return array
    
def ordenar_dos_arreglos(arreglo_a, arreglo_b):
    for i,numb in enumerate(arreglo_b):
        for j in range(len(arreglo_a)):
            if(numb == arreglo_a[j]):
                arreglo_a = insertar_valor(arreglo_a,numb,j)
                break
            elif(numb < arreglo_a[j]):
                arreglo_a = insertar_valor(arreglo_a,numb,j)
                break
        else:
            arreglo_a = insertar_valor(arreglo_a,numb,len(arreglo_a))
                
    return arreglo_a

print(ordenar_dos_arreglos(a,b))
    