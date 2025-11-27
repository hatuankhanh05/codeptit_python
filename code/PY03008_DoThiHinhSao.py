def solve():
    n = int(input())
    deg = [0] * (n + 1)
    for i in range(n - 1):
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1
    cnt1 = 0
    cnt2 = 0
    for i in range(1, n + 1):
        if deg[i] == n - 1:
            cnt1 += 1
        elif deg[i] == 1:
            cnt2 += 1
    if cnt1 == 1 and cnt2 == n - 1:
        print("Yes")
    else:
        print("No")

t = 1
# t = int(input())
for _ in range(t):
    solve()