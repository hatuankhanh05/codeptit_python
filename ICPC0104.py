def solve():
    s = input()
    mn = -1
    i = 0
    while i < len(s):
        if s[i] >= '0' and s[i] <= '9':
            x = 0
            while i < len(s) and s[i] >= '0' and s[i] <= '9':
                x = x * 10 + int(s[i])
                i += 1
            mn = x if mn == -1 else min(mn, x)
        i += 1
    print(mn)

t = 1
t = int(input())
for _ in range(t):
    solve()