
a = [1,1,1,1,2]
b = [3,7]
c = [1,3,1]


def sumaDeValoresArray(array):
    resultado = 0
    for i in array:
        resultado += i
        
    return resultado

def equalStacks(h1, h2, h3):
    suma1 = 0
    for i in h1:
        suma1 += i
    suma2 = 0
    for i in h2:
        suma2 += i
    suma3 = 0
    for i in h3:
        suma3 += i
    
    if suma1 == suma2 == suma3:
        return suma1
    else:
        cilindroMayor = 0
        cilindroMediano = 0
        cilindroMenor = 0
        if(suma1 > suma2):
            if suma1 > suma3:
                if(suma2 > suma3):
                    cilindroMayor = h1
                    cilindroMediano = h2
                    cilindroMenor = h3
                else:
                    cilindroMayor = h1
                    cilindroMediano = h3
                    cilindroMenor = h2
            else:
                cilindroMayor = h3
                cilindroMediano = h1
                cilindroMenor = h2
        else:
            if(suma2 > suma3):
                if(suma1 > suma3):
                    cilindroMayor = h2
                    cilindroMediano = h1
                    cilindroMenor = h3
                else:
                    cilindroMayor = h2
                    cilindroMediano = h3
                    cilindroMenor = h1
            else:
                cilindroMayor = h3
                cilindroMediano = h2
                cilindroMenor = h1
            
    while sumaDeValoresArray(cilindroMayor) != sumaDeValoresArray(cilindroMenor) != sumaDeValoresArray(cilindroMediano):
        if(sumaDeValoresArray(cilindroMayor) >= sumaDeValoresArray(cilindroMediano)):
            cilindroMayor.pop(0)
        else:
            if(sumaDeValoresArray(cilindroMayor) >= sumaDeValoresArray(cilindroMenor)):
                cilindroMayor,cilindroMediano = cilindroMediano, cilindroMayor
                continue
            else:
                cilindroMayor,cilindroMediano,cilindroMenor = cilindroMediano, cilindroMenor, cilindroMayor
                continue
            
    return sumaDeValoresArray(cilindroMayor)

print(equalStacks(a,b,c))