#!/usr/bin/env python

# Naive Fibonacci algorithm

def fib(n):
    if n<=2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    return f

# Memoized DP algorithm

def dp_fib(n):
    memo = {}

    def dp_fib_(n):
        if n in memo:
            return memo[n]
        if n<=2:
            f = 1
        else:
            f = dp_fib_(n-1) + dp_fib_(n-2)
        memo[n] = f
        return f

    return dp_fib_(n)

# Log N algorithm

from math import floor, sqrt
def log_fib(n):
    phi = (1 + sqrt(5)) / 2.0
    return floor(phi**n / sqrt(5) + 1/2.0)

def main():
    print dp_fib(100)
    print log_fib(100)
    print fib(100)
    
if __name__ == "__main__":
    main()
