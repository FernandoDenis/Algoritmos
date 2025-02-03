class BitVector:
    def __init__(self, size):
        self.size = size  # Número total de bits
        self.wordSize = size  # Si quieres exactitud de tamaño en bits
        self.vector = [0] * ((size + self.wordSize - 1) // self.wordSize)

    def set(self, numeroEnt):
        if numeroEnt >= self.size:
            return False  # Fuera del rango del bitvector

        indxArray = numeroEnt // self.wordSize
        indxBit = numeroEnt % self.wordSize
        self.vector[indxArray] |= (1 << indxBit)
        return True

    def get(self, numeroEnt):
        if numeroEnt >= self.size:
            return False  # Fuera del rango del bitvector

        indxArray = numeroEnt // self.wordSize
        indxBit = numeroEnt % self.wordSize
        return (self.vector[indxArray] & (1 << indxBit)) != 0

    def __str__(self):
        # Para visualizar el vector completo como una cadena de bits
        return ''.join(bin(word)[2:].zfill(self.wordSize) for word in self.vector)
