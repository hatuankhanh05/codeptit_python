import math

def solve():
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    k = int(input())
    sum_above = 0
    sum_under = 0
    for i in range(n):
        for j in range(n):
            if i + j < n - 1:
                sum_above += a[i][j]
            elif i + j > n - 1:
                sum_under += a[i][j]
    diff = abs(sum_above - sum_under)
    print("YES" if diff <= k else "NO")
    print(diff)

t = 1
# t = int(input())
for _ in range(t):
    solve()