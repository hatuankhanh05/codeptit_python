def solve():
    n, m = map(int, input().split())
    a = [[] for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    rmvi = [0] * n
    rmvj = [0] * m
    i = 0
    cnt = 0
    while i < n and n - cnt > m:
        rmvi[i] = 1
        cnt += 1
        i += 2
    i = 1
    cnt2 = 0
    while i < m and m - cnt2 > n - cnt:
        rmvj[i] = 1
        cnt2 += 1
        i += 2
    for i in range(n):
        if rmvi[i] == 1:
            continue
        for j in range(m):
            if rmvj[j] == 1:
                continue
            print(a[i][j], end = " ")
        print()

t = 1
# t = int(input())
for _ in range(t):
    solve()