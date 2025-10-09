import math

def gcd(a, b):
    while a * b:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def solve():
    n = int(input())
    k = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            k += 1
    print("YES" if is_prime(k) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()