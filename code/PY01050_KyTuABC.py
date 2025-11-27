def Try(s, n, cnt0, cnt1, cnt2):
    if len(s) == n:
        if cnt0 > 0 and cnt0 <= cnt1 and cnt1 <= cnt2:
            print(s)
        return
    Try(s + 'A', n, cnt0 + 1, cnt1, cnt2)
    Try(s + 'B', n, cnt0, cnt1 + 1, cnt2)
    Try(s + 'C', n, cnt0, cnt1, cnt2 + 1)

def solve():
    n = int(input())
    for m in range(3, n + 1):
        Try("", m, 0, 0, 0)

t = 1
# t = int(input())
for _ in range(t):
    solve()