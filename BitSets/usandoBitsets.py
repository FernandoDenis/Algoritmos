binNumber = 0b00001010

class BitVector:
    def __init__(self, size):
        self.size = size
        self.vector = [0] * size
        self.wordSize = 64

    def set(self,numeroEnt):
        indxArray = numeroEnt // self.wordSize
        indxBit = numeroEnt % self.wordSize

        if(indxArray >= self.size): return False

        self.vector[indxArray] |= (1 << indxBit)
        return indxArray, indxBit
    
    def get(self,numeroEnt):
        indxArray = numeroEnt // self.wordSize
        indxBit = numeroEnt % self.wordSize

        return (self.vector[indxArray] & (1 << indxBit) != 0)
    
    # incompleto
    def nextFalse(self,numeroEnt):
        # Se le suma 1 para empezar a comparar desde el siguiente bit
        numeroEnt += 1
        
        indxArray = numeroEnt // self.wordSize
        indxBit = numeroEnt % self.wordSize

        # Realiza una operacion AND para comparar si el bit esta en 1 o no
        while(self.vector[indxArray] & (1 << indxBit) != 0):
            indxBit += 1

            # Esta condicion es cuando terminan los bits en una posicion del array, para que pase a la siguiente posicion
            if(indxBit > (self.wordSize - 1)):
                indxArray += 1
                indxBit = 0

        return indxBit + (indxArray * self.wordSize)
    
    def prevFalse(self, numeroEnt):
        if(numeroEnt == 0): return False

        # Se le resta 1 para empezar a comparar desde el anterior bit
        numeroEnt -= 1
        
        indxArray = numeroEnt // self.wordSize
        indxBit = numeroEnt % self.wordSize

        # Realiza una operacion AND para comparar si el bit esta en 1 o no
        while(self.vector[indxArray] & (1 << indxBit) != 0):
            indxBit -= 1

            # Esta condicion es cuando terminan los bits en una posicion del array, para que pase a la siguiente posicion
            if(indxBit < 0):
                indxArray -= 1
                indxBit = (self.wordSize - 1)

            if(indxArray < 0): return False

        return indxBit + (indxArray * self.wordSize)
    
    def foundUnique(self):
        indxArray = 0
        indxBit = 0

        while(self.vector[indxArray] == ((1 << self.wordSize) - 1)):
            indxArray += 1

            if(indxArray >= self.size):
                return False
        
        while(self.vector[indxArray] & (1 << indxBit) != 0):
            indxBit += 1

        return indxBit + (indxArray * self.wordSize)

        
# prSet = BitVector(100000000)

# for i in range(0,1000000000):
#     prSet.set(i)

# print(prSet.foundUnique())

# print(prSet.vector)

# print(prSet.set(31))
# print(prSet.set(32))

# print(prSet.vector)

# print(f"Siguiente: {prSet.nextFalse(30)}")

# print(f"Anterior: {prSet.prevFalse(32)}")

# print(prSet.vector)