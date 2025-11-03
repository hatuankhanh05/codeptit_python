def toScore(n):
    if n >= 39:
        return 9.0
    if n >= 37:
        return 8.5
    if n >= 35:
        return 8.0
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
    return 0

def finalScore(score):
    r = score - int(score)
    if r >= 0.75:
        return int(score) + 1.0
    if r >= 0.25:
        return int(score) + 0.5
    return float(int(score))

def solve():
    arr = input().split()
    r, l = map(int, arr[0:2])
    ss, ws = map(float, arr[2:])
    rs = toScore(r)
    ls = toScore(l)
    tot = rs + ls + ss + ws
    avg = tot / 4
    print(finalScore(avg))

T = int(input())
for _ in range(T):
    solve()