def dfs(u, vst, adj, comp, cnt):
    vst[u] = 1
    comp[u] = cnt
    for v in adj[u]:
        if vst[v] != 1:
            dfs(v, vst, adj, comp, cnt)

def solve():
    n, m, x = map(int, input().split())
    x -= 1
    adj = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    comp = [0] * n
    vst = [0] * n
    cnt = 0
    for i in range(n):
        if vst[i] != 1:
            dfs(i, vst, adj, comp, cnt)
            cnt += 1
    for i in range(n):
        if i == x:
            continue
        if comp[i] != comp[x]:
            print(i + 1)

t = 1
# t = int(input())
for _ in range(t):
    solve()