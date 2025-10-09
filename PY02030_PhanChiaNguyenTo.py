import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    f = [0] * 1001
    for x in a:
        f[x] += 1
    b = [-1]
    for x in a:
        if f[x] > 0:
            b.append(x)
            f[x] = 0
    pref_b = [0] * len(b)
    for i in range(1, len(b)):
        pref_b[i] = pref_b[i - 1] + b[i]
    for i in range(1, len(b)):
        if isPrime(pref_b[i]) and isPrime(pref_b[len(b) - 1] - pref_b[i]):
            print(i - 1)
            return
    print("NOT FOUND")

t = 1
# t = int(input())
for _ in range(t):
    solve()