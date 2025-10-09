from math import sqrt

def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0: return False
    return x > 1

def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            print(1 if isPrime(a[i][j]) else 0, end=" ")
        print()

t = 1
# t = int(input())
for _ in range(t):
    solve()