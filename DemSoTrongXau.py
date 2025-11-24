'''
    author: htkhanh05
    created at: 24.11.2025 08:12:56
'''

def solve():
    s = input()
    n = input()
    dist = len(n)
    i = 0
    cnt = 0
    while i < len(s):
        if s[i:i+dist] == n:
            cnt += 1
            i += dist
        else:
            i += 1
    print(cnt)

t = 1
t = int(input())
for _ in range(t):
    solve()