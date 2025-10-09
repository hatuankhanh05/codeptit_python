def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [a[-1] * a[-2], a[0] * a[1], a[-1] * a[-2] * a[-3], a[0] * a[1] * a[-1]]
    res = max(ans)
    print(res)

t = 1
# t = int(input())
for _ in range(t):
    solve()