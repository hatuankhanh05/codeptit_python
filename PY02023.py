import math

def sod(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a, key = lambda x : (sod(x), x))
    for x in b:
        print(x, end = " ")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()