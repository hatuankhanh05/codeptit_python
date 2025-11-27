import sys

def isWord(x):
    if len(x) == 1 and not x[0].isalnum():
        return False
    return True

def solve():
    for line in sys.stdin:
        x = line.strip().split()
        endChar = '.'
        if not isWord(x[-1]):
            endChar = x[-1]
            x.pop()
        x[0] = x[0].capitalize()
        for i in range(1, len(x)):
            x[i] = x[i].lower()
        if not x[-1][-1].isalnum():
            x[-1] = x[-1][0:-1]
        ans = ' '.join(x)
        print(ans + endChar)

t = 1
# t = int(input())
for _ in range(t):
    solve()