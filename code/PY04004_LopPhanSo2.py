from math import gcd

class Fraction:
    def __init__(self, a, b):
        g = gcd(a, b)
        a //= g
        b //= g
        self.a = a
        self.b = b

    def __add__(self, other):
        aa = self.a * other.b + self.b * other.a
        bb = self.b * other.b
        return Fraction(aa, bb)

    def __str__(self):
        return f"{self.a}/{self.b}"

def solve():
    x, y, xx, yy = map(int, input().split())
    p = Fraction(x, y)
    q = Fraction(xx, yy)
    print(p + q)

t = 1
# t = int(input())
for _ in range(t):
    solve()