#Dos arreglos ordenados
a = [1,2,5]
b = [0,3,3,7,8,9,10]
    
def ordenar_dos_arreglos(arreglo_a,arreglo_b):
    #Puntero del final del arreglo a
    last_a_index = len(arreglo_a) - 1
    
    #Aumentando el tamaño del array(a) para puedan entrar los dos arreglos
    for i in range(len(arreglo_b)):
        arreglo_a.append(None)
    
    #Puntero del final de la suma del arreblo a y b
    final_index = len(arreglo_a) - 1
    
    #Puntero del arreglo b
    i = len(arreglo_b) - 1
    
    while(i >= 0):
        #Si el ultimo indice se pasa del 0 pero falta la posicion 0 en el arreglo b
        if(last_a_index == -1 and i == 0):
            arreglo_a[final_index] = arreglo_b[i]
            i -= 1
        #Si el ultimo numero del arreglo b es menor o igual al ultimo numero del arreglo a
        elif(arreglo_b[i] <= arreglo_a[last_a_index]):
            arreglo_a[final_index] = arreglo_a[last_a_index]
            arreglo_a[last_a_index] = None
            final_index -= 1
            last_a_index -= 1
        #Si el ultimo numero del arreglo b es mayor que el ultimo numero del arreglo a
        else: 
            arreglo_a[final_index] = arreglo_b[i]
            arreglo_b[i] = None
            final_index -= 1
            i -= 1
    
    return arreglo_a

print(ordenar_dos_arreglos(a,b))