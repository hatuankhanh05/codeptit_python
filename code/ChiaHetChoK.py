def solve():
    a, k, n = map(int, input().split())
    hasAny = False
    for c in range(k, n + 1, k):
        if c - a < 1: continue
        hasAny = True
        print(c - a, end=" ")
    if not hasAny:
        print(-1)

t = 1
# t = int(input())
for _ in range(t):
    solve()