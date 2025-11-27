import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    primes = []
    for x in a:
        if isPrime(x):
            primes.append(x)
    primes.sort()
    idx = 0
    for i in range(n):
        if isPrime(a[i]):
            print(primes[idx], end = " ")
            idx += 1
        else:
            print(a[i], end = " ")

t = 1
# t = int(input())
for _ in range(t):
    solve()