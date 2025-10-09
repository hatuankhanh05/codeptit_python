def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n - 1):
        mx = max(a[i], a[i + 1])
        mn = min(a[i], a[i + 1])
        if mn * 2 >= mx:
            continue
        else:
            while mn * 2 < mx:
                cnt += 1
                mn *= 2
    print(cnt)

t = 1
t = int(input())
for _ in range(t):
    solve()