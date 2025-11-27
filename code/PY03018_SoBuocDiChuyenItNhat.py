import sys
import collections

inf = 10**3

def solve(n, m, a):
    q = []
    dp = [[inf] * m for i in range(n)]
    dp[0][0] = 0
    q = collections.deque([(0, 0)])
    while q:
        i, j = q.popleft()
        d = dp[i][j]
        if i + 1 < n:
            step = abs(a[i + 1][j] - a[i][j])
            newi = i + step
            if newi < n and dp[newi][j] > d + 1:
                dp[newi][j] = d + 1
                q.append((newi, j))
        if j + 1 < m:
            step = abs(a[i][j + 1] - a[i][j])
            newj = j + step
            if newj < m and dp[i][newj] > d + 1:
                dp[i][newj] = d + 1
                q.append((i, newj))
        if i + 1 < n and j + 1 < m:
            step = abs(a[i + 1][j + 1] - a[i][j])
            newi = i + step
            newj = j + step
            if newi < n and newj < m and dp[newi][newj] > d + 1:
                dp[newi][newj] = d + 1
                q.append((newi, newj))
    ans = dp[n - 1][m - 1]
    return -1 if ans == inf else ans

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); m = int(data[idx + 1])
        idx += 2
        a = []
        for i in range(n):
            row = list(map(int, data[idx:idx + m]))
            idx += m
            a.append(row)
        out.append(str(solve(n, m, a)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()