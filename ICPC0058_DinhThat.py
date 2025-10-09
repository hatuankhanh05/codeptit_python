def dfs(x, adj, rm, u, v, vst):
    vst[x] = 1
    if x == v: 
        return
    for y in adj[x]:
        if y == rm:
            continue
        if vst.get(y, 0) == 0:
            dfs(y, adj, rm, u, v, vst)

def solve():
    n, m, u, v = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
    cnt = 0
    for i in range(1, n + 1):
        if i == u or i == v:
            continue
        vst = {}
        dfs(u, adj, i, u, v, vst)
        if vst.get(v, 0) == 0:
            cnt += 1
    print(cnt)

t = 1
t = int(input())
for _ in range(t):
    solve()