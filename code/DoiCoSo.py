'''
    author: htkhanh05
    created at: 27.11.2025 12:44:34
'''
base = []

def calBase():
    for i in range(10):
        base.append(i)
    for i in range(26):
        base.append(chr(ord('A') + i))

def solve():
    n, b = map(int, input().split())
    ans = []
    while n > 0:
        ans.append(str(base[n % b]))
        n //= b
    ans.reverse()
    res = ''.join(ans)
    print(res)

t = 1
calBase()
t = int(input())
for _ in range(t):
    solve()