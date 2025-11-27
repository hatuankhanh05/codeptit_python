'''
    author: htkhanh05
    created at: 17.11.2025 08:40:57
'''
import math

primes = []

def precompute():
    global primes
    a = [True] * 20001
    a[0] = a[1] = False
    for i in range(2, int(math.sqrt(20000)) + 1):
        if a[i]:
            for j in range(i * i, 20001, i):
                a[j] = False
    for i in range(20001):
        if a[i]:
            primes.append(i)

def lower_bound(x):
    global primes
    lo = 0
    hi = len(primes) - 1
    pos = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if primes[mid] >= x:
            pos = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return pos

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    precompute()
    step = 0
    for i in range(n):
        pos = lower_bound(a[i])
        prevPos = None
        nextPos = None
        if pos > 0:
            prevPos = pos - 1
        if pos < len(primes) - 1:
            nextPos = pos + 1
        adding = abs(a[i] - primes[pos])
        if prevPos:
            adding = min(adding, abs(a[i] - primes[prevPos]))
        if nextPos:
            adding = min(adding, abs(a[i] - primes[nextPos]))
        step = max(step, adding)
    print(step)

t = 1
#t = int(input())
for _ in range(t):
    solve()