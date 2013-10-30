#!/usr/bin/env python

class DisjointSet:
    def __init__(self):
        #self.set = []
        self.parent = []
        self.d = {}
        self.reverse_d = {}
        self.counter = 0
    def find(self, a_):
        return self.reverse_d[ self.find_( self.d[a_] ) ]
    def find_(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find_(self.parent[a])
        return self.parent[a]
    def make_set(self, a_):
        self.d[a_] = self.counter
        a = self.d[a_]
        self.reverse_d[a] = a_
        self.parent.append(a)
        self.counter += 1
    def union(self, a_, b_):
        ra = self.find_(self.d[a_])
        rb = self.find_(self.d[b_])
        self.parent[rb] = ra

def main():
    d = DisjointSet()

    # Test with integers
    for i in range(0,9):
        d.make_set(i)

    d.union(0,2)
    d.union(2,3)
    d.union(1,5)
    d.union(4,6)
    d.union(6,8)
    d.union(3,7)
    
    assert(0==d.find(7))
    assert(1==d.find(1))
    assert(4==d.find(8))
    assert(4==d.find(4))


if __name__ == "__main__":
    main()
