def solve():
    import sys
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    c = list(map(int, input().split()))

    A, *X = map(int, input().split())
    B, *Y = map(int, input().split())

    setX = set(X)
    setY = set(Y)

    G, Aonly, Bonly, O = [], [], [], []
    for i in range(N):
        idx = i + 1
        if idx in setX and idx in setY:
            G.append(c[i])
        elif idx in setX:
            Aonly.append(c[i])
        elif idx in setY:
            Bonly.append(c[i])
        else:
            O.append(c[i])

    G.sort()
    Aonly.sort()
    Bonly.sort()
    O.sort()

    INF = 10**18
    ans = INF

    # prefix sums
    def prefix(arr):
        pre = [0]
        for v in arr:
            pre.append(pre[-1] + v)
        return pre

    preG = prefix(G)
    preA = prefix(Aonly)
    preB = prefix(Bonly)

    for g in range(min(len(G), M) + 1):
        needA = max(0, K - g)
        needB = max(0, K - g)

        if needA > len(Aonly) or needB > len(Bonly):
            continue

        used = g + needA + needB
        if used > M:
            continue

        cost = preG[g] + preA[needA] + preB[needB]

        remain = M - used
        pool = []
        pool.extend(G[g:])
        pool.extend(Aonly[needA:])
        pool.extend(Bonly[needB:])
        pool.extend(O)
        pool.sort()

        if len(pool) < remain:
            continue

        cost += sum(pool[:remain])
        ans = min(ans, cost)

    print(ans if ans < INF else -1)

solve()