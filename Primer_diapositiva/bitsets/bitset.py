class bitset:
    data = [0] * 10
    def _init_(self, size):
        self.data = [0] * ((size // 64 ) +1)
    def set(self, bit):
        self.data[bit // 64] |= bit % 64
        
    def isset(self,bit):
        print (bit % 64)
        if self.data[bit // 64] | bit % 64 == 0:
            return False
        return True
    
    
a = bitset(256)
a.set(100)
print (a.isset(100))
print (a.isset(10))