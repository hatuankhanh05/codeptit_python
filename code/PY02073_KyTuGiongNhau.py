def solve():
    n = int(input())
    x, y, z = map(int, input().split())
    inf = 10 ** 9
    dp = [inf] * (n + 1)
    dp[0] = 0
    dp[1] = x
    for i in range(2, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + x)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[int(i / 2)] + z)
        else:
            dp[i] = min(dp[i], dp[int((i + 1) / 2)] + y + z)
    print(dp[n])

t = 1
t = int(input())
for _ in range(t):
    solve()