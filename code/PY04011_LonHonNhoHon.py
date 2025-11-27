import sys

sys.setrecursionlimit(2 * 10**5 + 5)

def solve():
    n = int(sys.stdin.readline())
    # n = int(input())
    mp = {}
    cnt = 0
    edges = []
    for _ in range(n):
        x, y, z = sys.stdin.readline().split()
        # x, y, z = input().split()
        if y == '<':
            x, z = z, x
        if x not in mp:
            mp[x] = cnt
            cnt += 1
        if z not in mp:
            mp[z] = cnt
            cnt += 1
        xx = mp[x]
        zz = mp[z]
        edges.append((xx, zz))
    adj = [[] for _ in range(cnt)]
    for (u, v) in edges:
        adj[u].append(v)
    vst = [0] * cnt

    def dfs(u):
        vst[u] = 1
        for v in adj[u]:
            if vst[v] == 0:
                if dfs(v):
                    return True
            if vst[v] == 1:
                return True
        vst[u] = 2
        return False
    
    ok = True
    for i in range(cnt):
        if vst[i] == 0:
            if dfs(i):
                ok = False
                break
    print("possible" if ok else "impossible")

t = 1
# t = int(input())
for _ in range(t):
    solve()