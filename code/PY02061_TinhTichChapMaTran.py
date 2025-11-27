def solve():
    n, m = map(int, input().split())
    imgMat = [[] for i in range(n)]
    for i in range(n):
        imgMat[i] = list(map(int, input().split()))
    kerMat = [[] for i in range(3)]
    for i in range(3):
        kerMat[i] = list(map(int, input().split()))
    resMat = [[0 for i in range(m - 3 + 1)] for i in range(n - 3 + 1)]
    x = 0
    for i in range(1, 1 + n - 3 + 1):
        y = 0
        for j in range(1, 1 + m - 3 + 1):
            tot = 0
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    tot += imgMat[i + ii][j + jj] * kerMat[1 + ii][1 + jj]
            resMat[x][y] = tot
            y += 1
        x += 1
    res = 0
    for i in range(n - 3 + 1):
        for j in range(m - 3 + 1):
            res += resMat[i][j]
    print(res)

t = 1
t = int(input())
for _ in range(t):
    solve()