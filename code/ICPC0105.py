def is_digit(c):
    return c >= '0' and c <= '9'

def solve():
    s = input()
    i = 0
    mx = -1
    while i < len(s):
        if is_digit(s[i]):
            x = 0
            while i < len(s) and is_digit(s[i]):
                x = x * 10 + int(s[i])
                i += 1
            mx = x if mx == -1 else max(mx, x)
        i += 1
    print(mx)

t = 1
t = int(input())
for _ in range(t):
    solve()