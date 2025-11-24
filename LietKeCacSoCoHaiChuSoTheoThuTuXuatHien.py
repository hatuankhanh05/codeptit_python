'''
    author: htkhanh05
    created at: 24.11.2025 07:58:35
'''

def solve():
    s = input()
    lst = []
    mp = {}
    for i in range(0, len(s), 2):
        ss = s[i:i+2]
        if (len(ss) < 2):
            break
        if (mp.get(ss, False) != False):
            continue
        mp[ss] = True
        lst.append(ss)
    for x in lst:
        print(x, end=' ')

t = 1
#t = int(input())
for _ in range(t):
    solve()