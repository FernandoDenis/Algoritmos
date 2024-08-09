h = [11,11,10,10,10]

def largestRectangle(h):
    maxBuilding = 0
    
    for i,value in enumerate(h):
        length = 1
        if(i - 1 != -1):
            izq = i - 1
            while izq != -1 and value <= h[izq]:
                length += 1
                izq -= 1
        if(i + 1 != len(h)):
            der = i + 1
            while der != len(h) and value <= h[der]:
                length += 1
                der += 1
        
        if (maxBuilding < value * length):
            maxBuilding = value * length
            
    return maxBuilding
                    
print(largestRectangle(h))
