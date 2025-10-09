import math

def cntWords(s):
    return len(s.split())

def solve():
    n = int(input())
    a = [input() for _ in range(n)]
    i = 0
    res = []
    while i < n:
        if cntWords(a[i]) == 7:
            res.append(2)
            i += 4
        else:
            while i < n and cntWords(a[i]) == 6:
                i += 2
            res.append(1)
    print(len(res))
    for r in res:
        print(r)

t = 1
# t = int(input())
for _ in range(t):
    solve()