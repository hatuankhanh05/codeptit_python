'''
    author: htkhanh05
    created at: 05.12.2025 14:47:10
'''

import math

MAX = 10**6 + 1
MOD = 10**9 + 7
isPrime = [True] * MAX
primes = []

def sieve():
    global isPrime, primes
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(math.sqrt(MAX)) + 1):
        if isPrime[i]:
            for j in range(i * i, MAX, i):
                isPrime[j] = False
    for i in range(2, MAX):
        if isPrime[i]:
            primes.append(i)

def legendre(n, p) :
    ans = 0
    while n > 0:
        ans += n // p
        n //= p
    return ans

def solve():
    global primes
    a, b = map(int, input().strip().split())
    ans = 1
    for prime in primes:
        if prime > b:
            break
        exp = legendre(b, prime) - legendre(a - 1, prime)
        if exp < 1:
            continue
        tmp = exp * 2 + 1
        ans = (ans * tmp) % MOD
    print(ans)

if __name__ == '__main__':
    sieve()
    t = 1
    t = int(input().strip())
    for _ in range(t):
        solve()