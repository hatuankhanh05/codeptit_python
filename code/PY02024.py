import math

def sod(n):
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a, key = lambda x: (sod(x), x))
    for x in b:
        print(x, end = " ")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()