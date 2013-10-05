#!/usr/bin/env python

# Kruskal's greedy algorithm for minimum spanning tree

from digraph import Graph, random_graph

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

def quick_sort(list, index_fxn):
    # split in half, sort each side
    if len(list) <= 1:
        return list
    
    head = list[0]
    left = []
    right = []
    for i in list[1:]:
        if index_fxn(i) <= index_fxn(head):
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left, index_fxn) + [head] + quick_sort(right, index_fxn)

def kruskal(graph):
    dset = DisjointSet()
    
    A = []
    for v in graph.get_vertices():
        dset.make_set(v)
    # get edges and sort by increasing weight
    edges = graph.get_edges()
    edges = quick_sort(edges, lambda x: x.cost)
    for e in edges:
        print e.v1, e.v2, e.cost
    print

    # sort edges increasing by weight
    
    for e in edges:
        if dset.find(e.v1) != dset.find(e.v2):
            A.append(e)
            dset.union(e.v1, e.v2)
    for e in A:
        print e.v1, e.v2, e.cost
    print

def main():
    graph = random_graph(5)
    print graph
    kruskal(graph)

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
    
    print d.find(7)
    print d.find(1)
    print d.find(8)
    print d.find(4)

    # Test with arbitrary node names
    d = DisjointSet()
    d.make_set("pineapple")
    d.make_set("coconut")
    d.make_set("happy")
    d.make_set("sad")
    d.make_set("morose")
    print "union"
    d.union("pineapple", "coconut")
    print "union"
    d.union("happy","sad")
    print "union"
    d.union("sad","morose")
    
    print d.find("morose")
    print d.find("coconut")




if __name__ == "__main__":
    main()
