def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(float, input().split())
        a.append(x)
        b.append(y)
    dp = [1] * n
    for i in range(n):
        for j in range(0, i):
            if a[i] > a[j] and b[i] < b[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))

t = 1
t = int(input())
for _ in range(t):
    solve()