def solve():
    n = int(input())
    a = [[] for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    k = int(input())
    totAbove = 0
    for i in range(n):
        for j in range(i + 1, n):
            totAbove += a[i][j]
    totUnder = 0
    for i in range(n):
        for j in range(0, i):
            totUnder += a[i][j]
    if abs(totAbove - totUnder) <= k:
        print("YES")
    else:
        print("NO")
    print(abs(totAbove - totUnder))

t = 1
# t = int(input())
for _ in range(t):
    solve()