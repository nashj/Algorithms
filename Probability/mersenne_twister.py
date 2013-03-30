
class MT:
    def __init__(self, seed):
        self.mt_length = 624
        self.mt = [0] * self.mt_length
        self.index = 0

        self.mt[0] = seed
        for i in range(1, self.mt_length):
            self.mt[i] = (1812433253 * (self.mt[i-1] ^ (self.mt[i-1] >> 30))) & 0xFFFFFFFF
        #self.generateNumbers()
        #print self.mt
        
    def getRand(self):
        if self.index == 0:
            self.generateNumbers()
        y = self.mt[self.index]
        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & (0x9D2C5680))
        y = y ^ ((y << 15) & (0xEFC60000))
        y = y ^ (y >> 18)
        self.index = (self.index + 1) % self.mt_length
        return y

    def generateNumbers(self):
        for i in range(0, self.mt_length):
            y = self.mt[i] & 0x80000000 + self.mt[(i+1)%self.mt_length] & 0x7FFFFFFF 
            self.mt[i] = self.mt[(i+397) % self.mt_length] ^ (y>>1)
            if (y % 2) != 0:
                self.mt[i] = self.mt[i] ^ 0x9908B0DF
                

if __name__ == "__main__":
    mt = MT(78)
    print mt.getRand()
    print mt.getRand()
    print mt.getRand()



    
