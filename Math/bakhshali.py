#!/usr/bin/env python
import math

def sqrt(S):
    #Bakhshali approximation

    # Find the nearest perfect square to S
    N = 1
    while (N+1)*(N+1) < S:
        N += 1
    
    # Approximation formula
    d = S - N*N
    P = d / 2 / N
    A = N + P
    return (A - P*P/2/A)

if __name__ == "__main__":
    print sqrt(3)
    print sqrt(5)
    print sqrt(9.2345)
    print sqrt(146)
