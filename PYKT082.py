import math

def toBase9(n):
    if n >= 39:
        return 9.0
    if n >= 37:
        return 8.5
    if n >= 35:
        return 8
    if n >= 33:
        return 7.5
    if n >= 30:
        return 7.0
    if n >= 27:
        return 6.5
    if n >= 23:
        return 6.0
    if n >= 20:
        return 5.5
    if n >= 16:
        return 5.0
    if n >= 13:
        return 4.5
    if n >= 10:
        return 4.0
    if n >= 7:
        return 3.5
    if n >= 5:
        return 3.0
    if n >= 3:
        return 2.5
    return 1.0

def isInteger(s):
    for c in s:
        if c == '.':
            return False
    return True

def solve():
    r, l, s, w = input().split()
    r = toBase9(int(r))
    l = toBase9(int(l))
    s = float(s)
    w = float(w)
    total = r + l + s + w
    total /= 4
    temp = total - int(total)
    res = float(int(total))
    if abs(temp - 0.75) < 1e-9: res += 1.0
    elif abs(temp - 0.25) < 1e-9: res += 0.5
    elif temp >= 0.75: res += 1.0
    elif temp >= 0.25: res += 0.5
    print("{:.1f}".format(res))

t = 1
t = int(input())
for _ in range(t):
    solve()