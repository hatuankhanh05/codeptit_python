def cntDig(n):
    dp = [0] * 10
    size = len(str(n))
    for i in range(size):
        pw = 10 ** i
        left = int(n / (pw * 10))
        mid = int(n / pw) % 10
        right = n % pw
        for j in range(10):
            if j == 0 and left == 0:
                continue
            if mid > j:
                dp[j] += (left + 1) * pw
            elif mid == j:
                dp[j] += left * pw + right + 1
            else:
                dp[j] += left * pw
            if j == 0:
                dp[j] -= pw
    return dp

def solve():
    a, b = map(int, input().split())
    x = cntDig(a - 1)
    y = cntDig(b)
    for i in range(10):
        print(y[i] - x[i], end = " ")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()