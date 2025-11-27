import math

def solve():
    n = int(input())
    a = [input() for i in range(n)]
    res = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] == 'C':
                cnt += 1
        if cnt > 1:
            res += cnt * (cnt - 1) // 2
    for j in range(n):
        cnt = 0
        for i in range(n):
            if a[i][j] == 'C':
                cnt += 1
        if cnt > 1:
            res += cnt * (cnt - 1) // 2
    print(res)

t = 1
# t = int(input())
for _ in range(t):
    solve()