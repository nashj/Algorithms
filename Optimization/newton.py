#!/usr/bin/env python
import math

def newton(f, f_prime, x_guess, err):
    x0 = 0
    x1 = x_guess
    while(abs(x1 - x0) > err):
        #print x1
        x0 = x1
        x1 = x0 - f(x0) / f_prime(x0)
    return x0

if __name__ == "__main__":
    x_guess = 5.0
    err = .001

    n1 = newton(lambda x: 3*x*x-5, lambda x: 6*x, x_guess, err)
    assert(abs(1.29099 - n1) <= err)

    x_guess = 3.5
    n1 = newton(lambda x: math.log(x*x), lambda x: 2*x, x_guess, err)
    assert(abs(1.0 - n1) <= err)
    
    
