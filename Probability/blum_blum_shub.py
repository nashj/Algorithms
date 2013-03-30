#!/usr/bin/env python

class BBS:
    def __init__(self, seed):
        p = 11
        q = 19
        self.M = p * q
        # The seed should be coprime to M
        self.x = seed
    def getRand(self):
        self.x = self.x**2 % self.M
        return (self.x % 2) # odd parity

if __name__ == "__main__":
    bbs = BBS(7)
    print bbs.getRand()

