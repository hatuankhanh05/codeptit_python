'''
    author: htkhanh05
    created at: 26.11.2025 17:48:18
'''

def countRisks(m, n, mat):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    cnt = 0
    vst = [[False] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if mat[i][j] == -1:
                for idx in range(8):
                    newi = i + dx[idx]
                    newj = j + dy[idx]
                    if newi < 0 or newi > m - 1 or newj < 0 or newj > n - 1:
                        continue
                    if vst[newi][newj]:
                        continue
                    vst[newi][newj] = True
                    cnt += mat[newi][newj]
    return cnt

def solve():
    m, n = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(m)]
    print(countRisks(m, n, mat))

t = 1
#t = int(input())
for _ in range(t):
    solve()