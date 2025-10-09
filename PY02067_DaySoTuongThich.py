def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    res = 10 ** 9
    for k in range(1, mx + 1):
        tot = 0
        can = True
        for i in range(n):
            val = a[i] // (k + 1) + 1
            if a[i] // val < k:
                can = False
                break
            tot += val
        if can:
            res = min(res, tot)
    print(res)

t = 1
# t = int(input())
for _ in range(t):
    solve()