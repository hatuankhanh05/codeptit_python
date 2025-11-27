import math

def solve():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    neg = []
    nonneg = []
    maxval = max(x)
    inserted = False
    for val in x:
        if val < 0:
            neg.append(val)
        else:
            if (val == maxval and not inserted):
                nonneg.append(m)
                inserted = True
            nonneg.append(val)
    for val in neg:
        print(val, end = " ")
    for val in nonneg:
        print(val, end = " ")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()