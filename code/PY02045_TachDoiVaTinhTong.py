def solve():
    s = input()
    while True:
        half = len(s) // 2
        a = s[0:half]
        b = s[half:]
        s = str(int(a) + int(b))
        print(s)
        if len(s) == 1:
            break

t = 1
# t = int(input())
for _ in range(t):
    solve()