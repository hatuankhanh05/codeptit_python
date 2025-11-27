def solve():
    n, m = map(int, input().split())
    a = [[] for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    mx = -1
    mn = -1
    for i in range(n):
        for j in range(m):
            mx = max(mx, a[i][j]) if mx != -1 else a[i][j]
    for i in range(n):
        for j in range(m):
            mn = min(mn, a[i][j]) if mn != -1 else a[i][j]
    luckyVal = mx - mn
    luckyPos = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == luckyVal:
                luckyPos.append((i, j))
    if len(luckyPos) < 1:
        print("NOT FOUND")
        return
    print(luckyVal)
    for (i, j) in luckyPos:
        print("Vi tri " + "[" + str(i) + "]" + "[" + str(j) + "]")

t = 1
# t = int(input())
for _ in range(t):
    solve()