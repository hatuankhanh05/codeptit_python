def solve():
    M, N = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    vst = [[False] * N for _ in range(M)]
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    ans = 0
    for i in range(M):
        for j in range(N):
            if A[i][j] == -1:
                for idx in range(8):
                    newi = i + di[idx]
                    newj = j + dj[idx]
                    if newi < 0 or newi > M - 1:
                        continue
                    if newj < 0 or newj > N - 1:
                        continue
                    if vst[newi][newj]:
                        continue
                    ans += A[newi][newj]
                    vst[newi][newj] = True
    print(ans)

solve()