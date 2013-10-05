#!/usr/bin/env python

'''
class Qubit:
    def __init__(self, state=0):
        self.a = 0
        self.b = 0
    def measure(self):
        pass

class QuantumComputer:
    def __init__(self, number_of_qubits):
        self.qubits = []
        for i in range(0, number_of_qubits):
            self.qubits.append(Qubit())
    def measure(self, qubits):
        pass
'''

import numpy as np
import math

class QuantumComputer:
    def __init__(self, bits):
        self.qubits = [0] * 2**bits
        self.qubits[0] = 1
        self.num_bits = bits

    def randomize_state(self):
        for i,q in enumerate(self.qubits):
            self.qubits[i] = 1.0 / math.sqrt(2**self.num_bits)


    def test_order(self):
        # Assume 3 qubits
        print self.qubits
        self.apply_transform( self.H(), 2 )
        print self.qubits
        self.apply_transform( self.CNOT(), 1 )
        print self.qubits        

    def test_teleportation(self):
        # assuming num_bits = 3

        a = .6
        b = .8
        self.qubits[0] = a
        self.qubits[4] = b
        #self.qubits[1] = b
        
        #self.apply_transform( self.construct_transform(self.H(), 1) )
        #print 
        print self.qubits
        self.apply_transform( self.H(), 1 )
        print self.qubits
        self.apply_transform( self.CNOT(), 1 )
        print self.qubits
        self.apply_transform( self.CNOT(), 0 )        
        print self.qubits
        self.apply_transform( self.H(), 0 )        
        print self.qubits

        print self.qubits        
        if (self.measure(1) == 1):
            print "Applying X"
            self.apply_transform(self.X(), 2)
        print self.qubits

        print self.qubits
        if (self.measure(0) == 1): # CHANGED FROM 0
            print "Applying Z"
            self.apply_transform(self.Z(), 2)
        print self.qubits
        print "Final state:", self.qubits
        
    def test(self):
        A = np.ones((3,3))
        A = A + A
        A[0,1] = 5
        A[2,2] = 7
        A[2,0] = 3
        B = np.ones((4,4))
        B = B + B + B
        B[3,3] = 5
        B[1,2] = 4
        B[0,0] = 2
        print self.tensor_product(A,B)

        A = np.ones((2,2))
        A[0,0] = 3
        A[0,1] = 4
        A[1,0] = 5
        A[1,1] = 6
        print self.construct_transform(A, 1)

    def CNOT(self):
        G = np.zeros((4,4))
        G[0,0] = 1
        G[1,1] = 1
        G[3,2] = 1
        G[2,3] = 1
        return G

    def H(self):
        # Hadamard gate
        G = np.ones((2,2))
        G[1,1] = -1
        G = 1/math.sqrt(2) * G
        return G

    def X(self):
        # bit flip
        G = np.zeros((2,2))
        G[0,1] = 1
        G[1,0] = 1
        return G

    def Z(self):
        # Phase flip
        G = np.identity(2)
        G[1,1] = -1
        return G

    def apply_transform(self, G, qubit):
        T = self.construct_transform(G, qubit)
        print T
        self.new_qubits = [0] * len(self.qubits)
        # Matrix multiplication of the state vector probabilities with the unitary transformation T
        for i in range(len(self.qubits)):
            new_val = 0
            for j in range(len(self.qubits)):    
                new_val += self.qubits[j] * T[i,j]
            self.new_qubits[i] = new_val
        for i in range(len(self.qubits)):
            self.qubits[i] = self.new_qubits[i]
            
    def construct_transform(self, G, qubit):
        # Question: how would you do a CNOT gate from, say, qubit 1 to qubit 4 (not adjacent?). I only know the 4x4 matrix representation for CNOT. 
        if (qubit > 0):
            A = np.identity(2**qubit)
            B = self.tensor_product(A, G)
        else:
            B = G

        C_size = self.num_bits - (qubit + int(math.log(G.shape[0],2)))
        if (C_size > 0):
            C = np.identity(2**C_size)
            C = self.tensor_product(B, C)
        else:
            C = B
        return C


    #def tensor_product_states(self, 
        
    def tensor_product(self, A, B):
        new_dim = A.shape[0]*B.shape[0]
        C = np.zeros((new_dim, new_dim))
        for i in range(new_dim):
            for j in range(new_dim):
                #print int(math.floor(i/A.shape[0]))
                #print int(math.floor(j/A.shape[1]))
                #print i % B.shape[0]
                #print j % B.shape[1]
                #print
                C[i,j] = A[int(math.floor(i/B.shape[0])), int(math.floor(j/B.shape[1]))] * B[i % B.shape[0], j % B.shape[1]]
        return C

    def measure(self, qubit):
        # find all numbers for which qubit = 1

        # I wrote the measure routine backwards (so in a 3 qubit system, measuring 0 measures 2), so this flips it back
        qubit = self.num_bits - 1 - qubit 

        one_prob = 0
        for i,q in enumerate(self.qubits):
            if ((i>>qubit)&0x1):
                one_prob += q*q

        # We already know prob of numbers for which qubit = 0
        # Randomly choose one or the other
        print "Probability of ones existing:", one_prob
        if one_prob > 1:
            one_prob = 1

        collapsed_value = np.random.binomial(1, one_prob)
        # Collapse all non-chosen, and renormalize the remaining coefficients
        renormalizing_total = 0
        for i,q in enumerate(self.qubits):
            if (((i>>qubit)&0x1) == 1-collapsed_value):
                self.qubits[i] = 0
            else:
                renormalizing_total += q*q

        print "Renormalizing total: ", renormalizing_total

        renormalizing_total = math.sqrt(renormalizing_total)
        for i,q in enumerate(self.qubits):
            self.qubits[i] = 1.0 * self.qubits[i] / renormalizing_total

        return collapsed_value

def main():
    '''
    qc = QuantumComputer(3)
    print "Measuring qubit 1:"
    print qc.randomize_state()
    print qc.measure(1)
    print qc.measure(1)
    print qc.measure(2)
    #print qc.measure(3)
    #print qc.measure(4)
    #print qc.measure(4)
    print qc.measure(1)
    qc.test()
    '''


    qc = QuantumComputer(3)
    qc.test_teleportation()


    '''
    qc = QuantumComputer(3)
    qc.test_order()
    '''
if __name__ == "__main__":
    main()
