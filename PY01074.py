import math

min_prime = [0] * 2000001

def sieve():
    for i in range(0, 2000001):
        min_prime[i] = i
    for i in range(2, int(math.sqrt(2000001)) + 1):
        if min_prime[i] == i:
            for j in range(i * i, 2000001, i):
                if min_prime[j] == j:
                    min_prime[j] = i

def solve():
    sieve()
    n = int(input())
    res = 0
    for i in range(n):
        x = int(input())
        while x > 1:
            res += min_prime[x]
            x //= min_prime[x]
    print(res)

t = 1
# t = int(input())
for _ in range(t):
    solve()