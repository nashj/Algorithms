#!/usr/bin/env python
import math

def rk4(y_start, t_start, t_end, h, f):
    # h is step size
    # y0 is the initial condition
    # f is: y' = f(t,y)
    # tend is the simulation final time
    y_solution = [y_start]
    t_solution = [t_start]
    
    y = y_start
    t = t_start
    while abs(t - t_end) > 1e-8:
        k1 = f(t,y)
        k2 = f(t + .5*h, y + h*.5*k1)
        k3 = f(t + .5*h, y + h*.5*k2)
        k4 = f(t + h, y + h*k3)
        y = y + h * 1/6.0 * (k1 + 2*k2 + 2*k3 + k4)
        t = t + h
        y_solution.append(y)
        t_solution.append(t)
    return [y_solution, t_solution]

def test_fxn1(t, y):
    # Time independent
    return math.tan(y) + 1

if __name__ == "__main__":
    [y_solution, t_solution] = rk4(1.0, 1.0, 1.1, .025, test_fxn1)
    assert(y_solution == [1.0, 1.0669709944238714, 1.1416368644521755, 1.2282273081511712, 1.3378892560905198])
    print "Test passed."
