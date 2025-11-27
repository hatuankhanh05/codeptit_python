def solve():
    n = int(input())
    b = [[] for i in range(n)]
    for i in range(n):
        b[i] = list(map(int, input().split()))
    if n == 2:
        print(1, b[0][1] - 1)
        return
    a = [0] * n
    for i in range(n - 2):
        a[i] = b[i][i + 1] - b[i + 1][i + 2] + b[i][i + 2]
        a[i] //= 2
        a[i + 2] = b[i][i + 2] - a[i]
        a[i + 1] = b[i][i + 1] - a[i]

    for i in range(n):
        print(a[i], end = " ")

t = 1
# t = int(input())
for _ in range(t):
    solve()