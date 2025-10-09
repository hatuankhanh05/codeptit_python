def dfs(u, vst, adj, rm):
    vst[u] = 1
    for v in adj[u]:
        if v == rm:
            continue
        if vst[v] != 1:
            dfs(v, vst, adj, rm)

def solve():
    n, m = map(int, input().split())
    adj = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    choose = -1
    mxComp = 0
    mp = {}
    for i in range(n):
        cnt = 0
        vst = [0] * n
        for j in range(n):
            if j == i:
                cnt += 1
                continue
            if vst[j] != 1:
                cnt += 1
                dfs(j, vst, adj, i)
        mp[cnt] = 1
        if cnt > mxComp:
            choose = i
            mxComp = cnt
    if len(mp) == 1:
        print(0)
        return
    print(choose + 1)

t = 1
t = int(input())
for _ in range(t):
    solve()