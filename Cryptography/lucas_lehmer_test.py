#!/usr/bin/env python

import math

# Primality test for Mersenne number M = 2^p - 1
def lucas_lehmer(M):
    # Requirement: M is a Mersenne number
    s = 4
    p = math.log(M+1, 2)
    p = int(p)
    for i in range(0, p-2):
        s = ((s * s) - 2) % M
        print s
    return (s==0)

def main():
    # 2^3-1=7 is MP
    assert(lucas_lehmer(7))
    # 2^4-1=15 is not MP
    assert(not lucas_lehmer(15))
    # 2^5-1=31 is MP
    assert(lucas_lehmer(31))
    # 2^6-1=63 is not MP
    assert(not lucas_lehmer(63))
    print "Lucas Lehmer Mersennse primality tests succeeded."
        
if __name__ == "__main__":
    main()
