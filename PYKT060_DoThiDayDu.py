def solve():
    n = int(input())
    m = int(input())
    adj = [[] for i in range(n)]
    deg = [0] * n
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if u < v:
            u, v = v, u
        adj[u].append(v)
        deg[u] += 1
        deg[v] += 1
    for i in range(n):
        deg[i] += n - 1 - len(adj[i])
        

t = 1
# t = int(input())
for _ in range(t):
    solve()