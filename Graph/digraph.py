#!/usr/bin/env python

# Floyd Warshall 

class Digraph:
    def __init__(self):
        self.g = {}
    def add_edge(self, a, b, cost):
        if a not in self.g:
            self.g[a] = [(b,cost)]
        else:
            self.g[a].append((b, cost))
    def get_edges(self, a):
        if a not in self.g:
            return []
        else:
            return self.g[a]
    def __str__(self):
        return self.g.__str__()
    def get_vertices(self):
        return self.g.keys() # there could be nodes that only receive incoming connections, though
    
class Edge:
    def __init__(self, a, b, cost):
        self.v1 = a
        self.v2 = b
        self.cost = cost

class Graph:
    def __init__(self):
        self.digraph = Digraph()
        self.edges = []
    def add_edge(self, a, b, cost):
        self.edges.append(Edge(a,b,cost))
        self.digraph.add_edge(a,b,cost)
        self.digraph.add_edge(b,a,cost)
    def get_edges(self):
        return self.edges
    #def get_edges(self, a):
    #    return self.digraph.get_edges(a)
    def get_vertices(self):
        return self.digraph.get_vertices()
    def __str__(self):
        return self.digraph.__str__()

def random_digraph():
    # Random matrix
    import numpy as np

    digraph = Digraph()
    num_nodes = 20

    for i in range(0,num_nodes):
        for j in range(0,num_nodes):
            if i != j:
                x = np.random.randint(2) # 50% chance there is no edge
                if (x > 0):
                    x = np.random.randint(1, 100)
                    digraph.add_edge(i, j, x)
    return digraph

def random_graph(num_nodes):
    # Random matrix
    import numpy as np

    graph = Graph()

    for i in range(0,num_nodes):
        for j in range(i+1,num_nodes):
            x = np.random.randint(2) # 50% chance there is no edge
            if (x > 0):
                x = np.random.randint(1, 100)
                graph.add_edge(i, j, x)
    return graph

def main():
    g = random_digraph()
    print g

if __name__ == "__main__":
    main()
