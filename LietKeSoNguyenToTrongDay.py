import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return x > 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    freq = [0] * (10 ** 6 + 1)
    for x in a:
        freq[x] += 1
    for x in a:
        if freq[x] > 0 and isPrime(x):
            print(x, freq[x])
            freq[x] = 0

t = 1
# t = int(input())
for _ in range(t):
    solve()