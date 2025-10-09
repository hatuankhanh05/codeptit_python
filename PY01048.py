import math

def solve():
    n = int(input())
    res = 0
    k = 2
    while k * (k - 1) // 2 < n:
        if (n - k * (k - 1) // 2) % k != 0:
            k += 1
            continue
        a = (n - k * (k - 1) // 2) // k
        if a >= 1:
            res += 1
        k += 1
    print(res)

t = 1
t = int(input())
for _ in range(t):
    solve()