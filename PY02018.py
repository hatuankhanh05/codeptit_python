import math

def solve():
    n = int(input())
    se = {0}
    se.discard(0)
    for i in range(1, 30002):
        se.add(i)
    a = list(map(int, input().split()))
    for x in a:
        se.discard(x)
    se = list(se)
    print(se[0])

t = 1
# t = int(input())
for _ in range(t):
    solve()