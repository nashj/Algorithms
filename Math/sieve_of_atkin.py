#!/usr/bin/env python

import math

def sieve_of_atkin(limit):
    is_prime = [0] * (limit+1) 
    sqrt_limit = int(math.floor(math.sqrt(limit)))
    for x in range(1,sqrt_limit+1):
        for y in range(1,sqrt_limit+1):
            n = 4*x*x + y*y
            if (n<=limit) and ((n%12==1) or (n%12==5)):
                is_prime[n] = not is_prime[n]
            n = 3*x*x + y*y
            if (n<=limit) and (n%12==7):
                is_prime[n] = not is_prime[n]
            n = 3*x*x - y*y
            if (x>y) and (n<=limit) and (n%12==11):
                is_prime[n] = not is_prime[n]

    for n in range(5, sqrt_limit+1):
        if is_prime[n]:
            k = n*n
            while k <= limit:
                is_prime[k] = 0
                k += n*n
    primes = [2,3]
    for n in range(5, limit+1):
        if is_prime[n]:
            primes.append(n)
    return primes
            
def main():
    n = 58
    prime_list = sieve_of_atkin(n)
    print prime_list

    n = 13
    prime_list = sieve_of_atkin(n)
    print prime_list

    n = 1015
    prime_list = sieve_of_atkin(n)
    print prime_list

if __name__ == "__main__":
    main()

