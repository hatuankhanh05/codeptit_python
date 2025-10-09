import math

a = []

def calA():
    q = []
    q.append(("1", 0))
    q.append(("2", 1))
    while len(q) > 0:
        cur = q.pop(0)
        val = cur[0]
        cnt = cur[1]
        if cnt * 2 > len(val):
            a.append(val)
        if len(a) >= 1000:
            return
        q.append((val + "0", cnt))
        q.append((val + "1", cnt))
        q.append((val + "2", cnt + 1))

def solve():
    n = int(input())
    for i in range(n):
        print(a[i], end = " ")
    print()

calA()
t = 1
t = int(input())
for _ in range(t):
    solve()