
from bitSet import BitVector

class BloomFilter:
    
    def __init__(self, size, numHashes):
        self.size  = size
        self.memory = BitVector(size)
        self.hashes = numHashes
        
    def add(self, data):
        numHashes = self.hashes
        # Genero el numero de hashes necesarios con la palabra que quiero agregar
        for i in range(0,numHashes):
            word = f"{data}{i}"
            self.memory.set(hash(word) % self.size)
        return
    
    def contains(self,data):
        numHashes = self.hashes
        for i in range(0,numHashes):
            word = f"{data}{i}"
            if self.memory.get(hash(word) % self.size):
                return True
            else:
                return False
        return
        
blum = BloomFilter(100,3)

blum.add("Fernando")
blum.add("Perro")
print(blum.contains("Perro"))
print(bin(blum.memory.vector[0]))