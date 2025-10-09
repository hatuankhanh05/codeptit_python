def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    f = [0] * (m + 5)
    for x in a:
        f[x] += 1
    mx = 0
    for i in range(1, m + 1):
        mx = max(mx, f[i])
    mx2 = -1
    choose = -1
    for i in range(1, m + 1):
        if f[i] == 0:
            continue
        if f[i] == mx:
            continue
        if f[i] > mx2:
            mx2 = f[i]
            choose = i
        elif f[i] == mx2 and i < choose:
            choose = i
    print(choose if choose != -1 else "NONE")

t = 1
# t = int(input())
for _ in range(t):
    solve()