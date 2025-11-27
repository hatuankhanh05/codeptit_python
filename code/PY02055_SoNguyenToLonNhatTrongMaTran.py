import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return x > 1

def solve():
    n, m = map(int, input().split())
    a = [[] for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    maxPrime = -1
    for i in range(n):
        for j in range(m):
            if isPrime(a[i][j]):
                maxPrime = (max(maxPrime, a[i][j]) if maxPrime != -1 else a[i][j])
    if maxPrime == -1:
        print("NOT FOUND")
        return
    print(maxPrime)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxPrime:
                print("Vi tri " + "[" + str(i) + "]" + "[" + str(j) + "]")

t = 1
# t = int(input())
for _ in range(t):
    solve()