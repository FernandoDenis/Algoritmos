binNumber = 0b00001010

class BitVector:
    def __init__(self, size):
        self.size = size
        self.vector = [0] * size

    def set(self,numeroEnt):
        indxArray = numeroEnt // 32
        indxBit = numeroEnt % 32

        self.vector[indxArray] |= (1 << indxBit)
        return indxArray, indxBit
    
    def get(self,numeroEnt):
        indxArray = numeroEnt // 32
        indxBit = numeroEnt % 32

        return (self.vector[indxArray] & (1 << indxBit) != 0)
    
    # incompleto
    def nextFalse(self,bit):
        indxArray = bit // 32
        return
    
    # incompleto
    def prevFalse(self, bit):
        return

        
prSet = BitVector(100)

print(prSet.vector)

print(prSet.set(31))
print(prSet.set(30))

print(prSet.get(31))

# 