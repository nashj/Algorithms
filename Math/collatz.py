#!/usr/bin/env python

# Function based on the Collatz conjecture that computes n/2 for even numbers and 3*n+1 for odd numbers until the number reaches 1. 

# Returns a list of the sequence the number takes to reach 1
def collatzSequence(x):
    return collatzSequenceHelper(x, [])

def collatzSequenceHelper(x, ls):
    ls.append(x)
    if (1 == x):
        return ls
    elif (0 == x % 2): # Even
        return collatzSequenceHelper(x/2, ls)
    else:
        return collatzSequenceHelper(3*x + 1, ls)

if __name__ == "__main__":

    # Prints the Collatz number sequence
    for i in range(1,200):
        print collatzSequence(i)
        x = raw_input()
        


    



