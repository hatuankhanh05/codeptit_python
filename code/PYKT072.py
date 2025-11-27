import math

def solve():
    n = int(input())
    a = [input() for i in range(n)]
    minsteps = -1
    leng = len(a[0])
    for i in range(n):
        cnt = 0
        for j in range(n):
            if j == i:
                continue
            can = False
            for k in range(leng):
                if a[i] == a[j][k:] + a[j][0:k]:
                    can = True
                    break
                cnt += 1
            if not can:
                print(-1)
                return
        minsteps = (cnt if minsteps == -1 else min(minsteps, cnt))
    print(minsteps)

t = 1
# t = int(input())
for _ in range(t):
    solve()