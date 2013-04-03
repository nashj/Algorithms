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

def create_matrix(arr):
    m = Matrix(len(arr), len(arr[0]))
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
           m[i,j] = arr[i][j]
    return m

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
    # A must be a symmetric matrix with real entries
    # This is the Cholesky-Banachiewicz variant that computes row-by-row
    L = Matrix(A.rows,A.cols)
    for i in range(0,A.rows):
        for j in range(0,i+1):
            l_sum = 0
            for k in range(0,j):
                l_sum += L[i,k] * L[j,k]
            if i==j:
                L[i,j] = math.sqrt(A[j,j] - l_sum)
            else:
                L[i,j] = 1.0 / L[j,j] * (A[i,j] - l_sum)
    return L

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

def freivald(A,B,C):
    # Randomized algorithm that verifies if A*B=C. Runs in O(n^2)
    # Always returns yes if A*B=C, returns 'yes' on A*B!=C with probability 1/2
    import random

    # Create random nx1 0/1 vector
    r = Matrix(B.rows, 1)
    for i in range(0, B.rows):
        r[i,0] = random.randint(0,1)
    Br = mult(B,r)
    ABr = mult(A, Br)
    Cr = mult(C, r)
    P = subtract(ABr, Cr)
    for i in range(0, B.rows):
        if P[i,0] != 0:
            return False
    return True

if __name__ == "__main__":
    #vonMises Test
    p = create_matrix([[10,1],[8,1]])
    print p
    print vonMises(p)

    # Cholesky Test
    m = create_matrix([[8,3,2],[3,7,1],[2,1,9]])
    print m
    chol = cholesky(m)
    print "My Cholesky decomposition:"
    print chol
    chol_ans = create_matrix([[2.82843, 0.00000, 0.00000],[1.06066, 2.42384, 0.00000], [0.70711, 0.10314, 2.91365]])
    print "MATLAB Cholesky decomposition:"
    print chol_ans
    #d = subtract(chol_ans, chol)
    #print d

    # Freivald Test
    n = create_matrix([[5,6,8],[-4,5,7],[-4,-9,-6]])
    p = mult(m,n)
    #print "Multiplied matrix:"
    #print p
    print "Test correct multiplication"
    print freivald(m,n,p)
    print freivald(m,n,p)
    print freivald(m,n,p)

    print "Test incorrect multiplication"
    p[2,2] = 0
    print freivald(m,n,p)
    print freivald(m,n,p)
    print freivald(m,n,p)


