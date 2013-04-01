import math
import random

class Matrix:
    def __init__(self, rows, cols):
        # Zero-initialize matrix
        self.m = [[0.0 for i in range(0,cols)] for i in range(0,rows)]
        self.rows = rows
        self.cols = cols
        #print self.m
    def __str__(self):
        s = ""
        for row in self.m:
            for j in row:
                s += str(j) + " "
            s += "\n"
        return s
    def __getitem__(self, index):
        x,y = index
        return self.m[x][y]
    def __setitem__(self, index, value):
        x,y = index
        self.m[x][y] = value

#def diag(x):
    
def add(A, B):
    assert(A.rows == B.rows)
    assert(A.cols == B.cols)

    C = Matrix(A.rows, A.cols)
    for i in range(0,A.rows):
        for j in range(0,A.cols):
            C[i,j] = A[i,j] + B[i,j]
    return C

def subtract(A, B):
    assert(A.rows == B.rows)
    assert(A.cols == B.cols)

    C = Matrix(A.rows, A.cols)
    for i in range(0,A.rows):
        for j in range(0,A.cols):
            C[i,j] = A[i,j] - B[i,j]
    return C

def mult(A, B):
    assert(A.cols == B.rows)
    C = Matrix(A.rows, B.cols)
    for i in range(0, A.rows):
        for j in range(0, B.cols):
            dotp = 0
            for k in range(0, A.cols):
                dotp += A[i,k] * B[k,j]
            C[i,j] = dotp
    return C

def multScalar(A, s):
    B = Matrix(A.rows, A.cols)
    for i in range(0, A.rows):
        for j in range(0, A.cols):
            B[i,j] = A[i,j] * s
    return B

def divScalar(A, s):
    B = Matrix(A.rows, A.cols)
    for i in range(0, A.rows):
        for j in range(0, A.cols):
            B[i,j] = A[i,j] / s
    return B

def transpose(A):
    B = Matrix(A.cols, A.rows)
    for i in range(0, A.rows):
        for j in range(0, A.cols):
            B[j,i] = A[i,j]
    return B

def cholesky(A):
    pass

def norm(v):
    # Must be a column vector
    assert(v.cols == 1)
    n = 0
    for i in range(0, v.rows):
        n += (v[i,0] * v[i,0])
    return math.sqrt(n)

def normalize(v):
    n = norm(v)
    return divScalar(v, n)

def dotp(v, w):
    assert(v.cols == 1)
    assert(w.cols == 1)
    d = 0
    for i in range(0, v.rows):
        d += v[i][0] * w[i][0]
    return d
    
def vonMises(A):
    # Returns eigenvector with top eigenvalue
    b = Matrix(A.cols,1)
    for i in range(0,A.cols):
        b[i,0] = random.uniform(0,1)

    for i in range(0,100):
        b = mult(A,b)
        b = normalize(b)
    return b

if __name__ == "__main__":
    #m = Matrix(5,5)
    #n = Matrix(5,5)
    #m[1,1] = 5.0
    #m[0,2] = 8.0
    #m[3,4] = 9.0

    #n[1,1] = 6.0
    #n[2,0] = 7.0
    #print m
    #print n
    #print add(m,n)
    #print mult(m,n)
    #print transpose(m)

    p = Matrix(2,2)
    p[0,0] = 10
    p[0,1] = 1
    p[1,0] = 8
    p[1,1] = 1
    print p
    print vonMises(p)
