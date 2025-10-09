import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        for j in range(m):
            x = 1 if isPrime(a[i][j]) else 0
            print(x, end = " ")
        print()

t = 1
# t = int(input())
for _ in range(t):
    solve()