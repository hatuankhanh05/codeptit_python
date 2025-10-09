import math

def binToDec(s):
    ans = 0
    for ch in s:
        ans = ans * 2 + int(ch)
    return ans

def solve():
    binStr = input().strip()
    r = len(binStr) % 3
    if r == 0:
        r = 3
    lead0s = ""
    for i in range(3 - r):
        lead0s += "0"
    binStr = lead0s + binStr
    oct = []
    for i in range(0, len(binStr), 3):
        oct.append(binToDec(binStr[i : i + 3]))
    for x in oct:
        print(x, end = "")

t = 1
# t = int(input())
for _ in range(t):
    solve()