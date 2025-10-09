import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for x in a:
        if isPrime(x):
            freq[x] = freq.get(x, 0) + 1
    for x in freq:
        print(x, freq[x])

t = 1
# t = int(input())
for _ in range(t):
    solve()