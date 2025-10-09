import math

def solve():
    n, k = map(int, input().split())
    mp = {}
    a = []
    for x in input().split():
        if mp.get(x, False) == False:
            mp[x] = True
            a.append(x)
    a.sort()
    k = min(k, len(a))
    n = len(a)
    b = []
    for x in range(k):
        b.append(x)
    while True:
        for i in range(k):
            print(a[b[i]], end = " ")
        print()
        i = k - 1
        while i >= 0 and b[i] == n - k + i:
            i -= 1
        if i < 0:
            break
        b[i] += 1
        for j in range(i + 1, k):
            b[j] = b[j - 1] + 1

t = 1
# t = int(input())
for _ in range(t):
    solve()