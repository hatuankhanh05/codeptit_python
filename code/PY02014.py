import math

MAX = 2 * 10 ** 4
isPrime = [True] * (MAX + 1)
primes = []

def firstNotSmaller(x):
    low = 0
    high = len(primes) - 1
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if primes[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def firstNotGreater(x):
    low = 0
    high = len(primes) - 1
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if primes[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def calPrime():
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(math.sqrt(MAX)) + 1):
        if isPrime[i]:
            for j in range(i * i, MAX, i):
                isPrime[j] = False
    for i in range(2, MAX + 1):
        if isPrime[i]:
            primes.append(i)

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    minSteps = 0
    for i in range(n):
        x = a[i]
        l = primes[firstNotGreater(a[i])]
        r = primes[firstNotSmaller(a[i])]
        steps = min(abs(l - x), abs(r - x))
        minSteps = max(minSteps, steps)
    print(minSteps)

calPrime()
t = 1
# t = int(input())
for _ in range(t):
    solve()