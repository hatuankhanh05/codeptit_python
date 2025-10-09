import math

def binToDec(s):
    res = 0
    for c in s:
        res = res * 2 + int(c)
    return res

def solve():
    s = input()
    a = []
    for i in range(len(s) - 1, -1, -3):
        temp = s[max(0, i - 2) : i + 1]
        while len(temp) < 3:
            temp = "0" + temp
        a.append(binToDec(temp))
    for i in range(len(a) - 1, -1, -1):
        print(a[i], end = "")
    print()

t = 1
# t = int(input())
for _ in range(t):
    solve()