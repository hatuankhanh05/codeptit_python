class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a

    def __mul__(self, other):
        res = Matrix(self.n, other.m, [[0] * other.m for i in range(self.n)])
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    res.a[i][j] += self.a[i][k] * other.a[k][j]
        return res
    
    def printOut(self):
        a = self.a
        for i in range(self.n):
            for j in range(self.m):
                print(a[i][j], end = " ")
            print()

def solve():
    n, m = map(int, input().strip().split())
    a = [list(map(int, input().strip().split())) for i in range(n)]
    b = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][i]
    thisMat = Matrix(n, m, a)
    thatMat = Matrix(m, n, b)
    (thisMat * thatMat).printOut()

t = 1
t = int(input())
for _ in range(t):
    solve()