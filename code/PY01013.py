import math

def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def sod(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def solve():
    a, b = map(int, input().split())
    print("YES" if is_prime(sod(gcd(a, b))) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()