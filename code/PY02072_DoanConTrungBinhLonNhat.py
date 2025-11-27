def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    len = 0
    maxLen = 0
    for i in range(n):
        if a[i] == mx:
            len += 1
            maxLen = max(maxLen, len)
        else:
            len = 0
    print(maxLen)

t = 1
# t = int(input())
for _ in range(t):
    solve()