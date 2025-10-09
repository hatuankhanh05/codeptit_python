import math

def sod(s):
    tot = 0
    for ch in s:
        tot += int(ch)
    return str(tot)

def solve():
    s = input()
    if s[0] == "-":
        s = s[1:]
    steps = 0
    while True:
        s = sod(s)
        steps += 1
        if len(s) == 1:
            break
    print(steps)

t = 1
# t = int(input())
for _ in range(t):
    solve()