def solve():
    n = int(input())
    a = []
    for _ in range(n):
        s = input()
        m = len(s)
        i = 0
        while i < m:
            if s[i].isdigit():
                x = 0
                while i < m and s[i].isdigit():
                    x = x * 10 + int(s[i])
                    i += 1
                a.append(x)
            else:
                i += 1
    a.sort()
    for x in a:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()