import math

def solve():
    s = input()
    res = []
    tot = 0
    for ch in s:
        if ch.isdigit():
            tot += int(ch)
        else:
            res.append(ch)
    res.sort()
    print("".join(res) + str(tot))

t = 1
t = int(input())
for _ in range(t):
    solve()