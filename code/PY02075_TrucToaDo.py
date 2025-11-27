def solve():
    n = int(input())
    a = []
    for i in range(n):
        x, xx = map(int, input().split())
        a.append((x, xx))
    a.sort(key = lambda x: x[1])
    cnt = 0
    lastEnd = 0
    for (x, xx) in a:
        if x < lastEnd:
            continue
        cnt += 1
        lastEnd = xx
    print(cnt)

t = 1
t = int(input())
for _ in range(t):
    solve()