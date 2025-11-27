import math

myDict = {}

def solve():
    n = int(input())
    curTheme = ""
    blankBefore = True
    for _ in range(n):
        s = input()
        if len(s.split()) == 0:
            blankBefore = True
            continue
        isTheme = True if blankBefore else False
        if isTheme:
            curTheme = s
            blankBefore = False
            continue
        myDict[curTheme] = myDict.get(curTheme, 0) + 1
    for theme in myDict:
        print(theme + ": " + str(myDict[theme]))

t = 1
# t = int(input())
for _ in range(t):
    solve()