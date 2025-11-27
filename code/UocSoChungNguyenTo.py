from math import gcd, sqrt

def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0: return False
    return x > 1

def sod(x):
    ans = 0
    while x:
        ans += x % 10
        x //= 10
    return ans

def solve():
    a, b = map(int, input().split())
    g = gcd(a, b)
    print("YES" if isPrime(sod(g)) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()