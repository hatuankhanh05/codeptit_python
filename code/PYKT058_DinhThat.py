def dfs(x, en, vst, adj, rm):
    vst[x] = 1
    if x == en:
        return
    for y in adj[x]:
        if y == rm: continue
        if vst[y] != 1:
            dfs(y, en, vst, adj, rm)

def solve():
    n, m, u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj = [[] for i in range(n)]
    for i in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        adj[x].append(y)
    res = 0
    for i in range(n + 1):
        if i == u or i == v:
            continue
        vst = [0] * n
        dfs(u, v, vst, adj, i)
        if vst[v] != 1:
            res += 1
    print(res)

t = 1
t = int(input())
for _ in range(t):
    solve()