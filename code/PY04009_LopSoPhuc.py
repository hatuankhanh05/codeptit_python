class Complex:
    def __init__(self, r, i):
        self.r = r 
        self.i = i

    def __str__(self):
        r = self.r
        i = self.i
        neg = '-' if i < 0 else '+'
        return f"{r} {neg} {abs(i)}i"
    
    def __add__(self, other):
        r = self.r + other.r
        i = self.i + other.i
        return Complex(r, i)
    
    def __mul__(self, other):
        r = self.r * other.r - self.i * other.i
        i = self.r * other.i + self.i * other.r
        return Complex(r, i)
    
    def sqr(self):
        return self * self

def solve():
    a, b, c, d = map(int, input().split())
    c1 = Complex(a, b)
    c2 = Complex(c, d)
    res1 = (c1 + c2) * c1
    res2 = (c1 + c2).sqr()
    print(f"{res1}, {res2}")

t = 1
t = int(input())
for _ in range(t):
    solve()