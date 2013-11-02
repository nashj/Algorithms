#!/usr/bin/env python

def sieve_of_eratosthenes(n):
    # numbers = range(0, n+1)
    prime = [1] * (n+1) # len(numbers)
    p = 2
    while p <= n:
        i = 2*p
        while i <= n:
            prime[i] = 0
            i += p
        p += 1
    
    primes = []
    for i in range(2,n+1):
        if prime[i]:
            primes.append(i) 
    return primes

def main():
    n = 58
    prime_list = sieve_of_eratosthenes(n)
    print prime_list

    n = 13
    prime_list = sieve_of_eratosthenes(n)
    print prime_list

    n = 1015
    prime_list = sieve_of_eratosthenes(n)
    print prime_list

if __name__ == "__main__":
    main()

    
