def solve():
    N, M, L = map(int, input().split())
    imgMat = [list(map(int, input().split())) for i in range(N)]
    pref = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    resMat = [[0 for i in range(M - L + 1)] for i in range(N - L + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            ii = i - 1
            jj = j - 1
            pref[i][j] = pref[ii][j] + pref[i][jj] - pref[ii][jj] + imgMat[ii][jj]
    x = 0           
    div = L ** 2
    for i in range(1, N - L + 2):
        y = 0
        for j in range(1, M - L + 2):
            ii = i + L - 1
            jj = j + L - 1
            iii = i - 1
            jjj = j - 1
            val = pref[ii][jj] - pref[iii][jj] - pref[ii][jjj] + pref[iii][jjj]
            val = int(val / div)
            resMat[x][y] = val
            y += 1
            print(val, end = " ")
        print()

t = 1
t = int(input())
for _ in range(t):
    solve()