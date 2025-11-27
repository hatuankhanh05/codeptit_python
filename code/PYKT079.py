import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    has = {}
    mn = min(a)
    mx = max(a)
    for x in a:
        has[x] = True
    res = 0
    for x in range(mn, mx + 1):
        if has.get(x, False) == False:
            res += 1
    print(res)

t = 1
t = int(input())
for _ in range(t):
    solve()