'''
    author: htkhanh05
    created at: 04.12.2025 22:44:12
'''

import sys

def isNumber(x):
    for d in x:
        if not d.isdigit():
            return False
    return True

def solve():
    INT_MAX = 2147483647
    ans = []
    # data = sys.stdin.read().split()
    with open('DATA.in', 'r') as f:
        data = f.read().split()
    for x in data:
        if not isNumber(x) or int(x) < -INT_MAX or int(x) > INT_MAX:
            ans.append(x)
    ans.sort()
    print(*ans)

t = 1
#t = int(input())
for _ in range(t):
    solve()