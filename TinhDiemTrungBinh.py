def solve():
    n = int(input())
    a = list(map(float, input().split()))
    mn = min(a)
    mx = max(a)
    tot = 0
    cnt = 0
    for x in a:
        if x == mn: continue
        if x == mx: continue
        tot += x
        cnt += 1
    res = tot / cnt
    print(f"{res:.2f}")

t = 1
# t = int(input())
for _ in range(t):
    solve()