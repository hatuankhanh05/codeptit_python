def solve():
    s = input()
    n = input()
    cnt = 0
    i = 0
    m = len(n)
    while i + m <= len(s):
        if s[i:i + m] == n:
            cnt += 1
            i += m
        else:
            i += 1
    print(cnt)

t = 1
t = int(input())
for _ in range(t):
    solve()