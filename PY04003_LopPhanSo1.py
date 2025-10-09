import math

class Fraction:
    def __init__(self, nume, deno):
        g = math.gcd(nume, deno)
        nume //= g
        deno //= g
        self.nume = nume
        self.deno = deno

    def __str__(self):
        return f"{self.nume}/{self.deno}"

def solve():
    nume, deno = map(int, input().split())
    frac = Fraction(nume, deno)
    print(frac)

t = 1
# t = int(input())
for _ in range(t):
    solve()