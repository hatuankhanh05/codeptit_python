'''
    author: htkhanh05
    created at: 24.11.2025 07:58:35
'''

def solve():
    s = input()
    se = set()
    for i in range(0, len(s), 2):
        ss = s[i:i+2]
        if (len(ss) < 2):
            break
        se.add(int(ss))
    lst = list(se)
    lst.sort()
    for x in lst:
        print(x, end=' ')

t = 1
#t = int(input())
for _ in range(t):
    solve()