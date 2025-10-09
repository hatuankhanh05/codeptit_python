import math

def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def solve():
    a = int(input())
    b = int(input())
    print(gcd(a, b))

t = 1
t = int(input())
for _ in range(t):
    solve()