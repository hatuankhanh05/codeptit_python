from math import log2

MOD = 10 ** 9 + 7

def solve():
    n, k = map(int, input().split())
    a = 0
    while k > 0:
        b = int(log2(k))
        a += int(1 << b)
        k -= 2 ** b
    c = []
    while a > 0:
        c.append(a % 2)
        a //= 2
    res = 0
    for i in range(len(c) - 1, -1, -1):
        res = res + n ** i * c[i]
        res %= MOD
    print(res)

t = 1
t = int(input())
for _ in range(t):
    solve()