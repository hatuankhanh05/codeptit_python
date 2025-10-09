import math

def solve():
    n = int(input())
    grid = [input() for i in range(n)]
    res = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if grid[i][j] == 'C':
                count += 1
        if count > 1:
            res += count * (count - 1) // 2
    for j in range(n):
        count = 0
        for i in range(n):
            if grid[i][j] == 'C':
                count += 1
        if count > 1:
            res += count * (count - 1) // 2
    print(res)

t = 1
# t = int(input())
for _ in range(t):
    solve()