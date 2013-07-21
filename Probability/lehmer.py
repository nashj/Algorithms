#!/usr/bin/env python

import math

class Lehmer:
    def __init__(self, seed):
        self.state = seed
        self.g = math.pow(7,5) # Primite root modulo M31
        self.n = math.pow(2,31) - 1 # Mersenne prime M31
    def getRand(self):
        self.state = (self.g * self.state) % self.n
        return self.state

def main():
    # Use Park-Miller MINSTD paramters
    rng = Lehmer(19) # The seed must be coprime to the modulus n. 
    print rng.getRand()
    print rng.getRand()
    print rng.getRand()

if __name__ == "__main__":
    main()
