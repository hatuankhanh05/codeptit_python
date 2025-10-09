def solve():
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if c > d:
        c, d = d, c
    e = c + d
    aa = a[:e]
    tot1, tot2 = sum(aa[:c]), sum(aa[c:e])
    res = tot1 / c + tot2 / d
    print("{:.6f}".format(res))

t = 1
t = int(input())
for _ in range(t):
    solve()