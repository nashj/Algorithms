#!/usr/bin/env python

from math import ceil

def findIndex(key, list):
    # Recursive binary search
    # Return an index with value x in list 
    # list must be sorted
    # If item with value x does not exist, returns -1
    return findIndexRecursive(key, list, 0, len(list))
    
def findIndexRecursive(key, list, min, max):
    if (max-min) <= 0:
        return -1

    #print key
    #print min,max
    #y = raw_input()

    mid = (max+min)/2
    pivot = list[ mid ]
    #print pivot
    if (key == pivot):
        return mid
    elif (key < pivot):
        # Look in first half of list
        return findIndexRecursive(key, list, min, mid)
    else:
        # Look in second half of list
        return findIndexRecursive(key, list, mid+1, max)

if __name__ == "__main__":
    # Standard checks
    assert(1 == findIndex(2, [1,2,3,4,5,6,7,8,9]))
    assert(8 == findIndex(2, [1,1,1,1,1,1,1,1,2]))
    assert(-1 == findIndex(10, [1,3,4,5,7,8]))
    assert(-1 ==  findIndex(0, [1,3,4,5,7,8]))
    assert(2 == findIndex(4, [1,3,4,5,7,8]))

    # Randomly generate lists to check
    import random
    
    # These lists will always have the value in the list
    for i in range(0,1000):
        # Construct list
        state = 0
        test_list = []
        test_list.append(state)
        for j in range(0,100):
            state += random.randint(0,1)
            test_list.append(state)
        #print test_list

        val = random.randint(0,state)
        #print val
        ind = findIndex(val, test_list)
        #print ind
        assert(val == test_list[ind])

    # These lists do not contain the value in the list

    print "Tests passed!"
