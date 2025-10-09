def solve():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    tot1 = 0
    tot2 = 0
    for i in range(n):
        for j in range(n):
            if i < j: tot1 += a[i][j]
            elif i > j: tot2 += a[i][j]
    diff = abs(tot1 - tot2)
    print("YES" if diff <= k else "NO")
    print(diff)

t = 1
# t = int(input())
for _ in range(t):
    solve()