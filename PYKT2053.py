'''
    author: htkhanh05
    created at: 26.11.2025 22:27:06
'''

def solve():
    n = int(input()) 
    a = list(map(int, input().split()))
    tot = 0
    for x in a:
        tot += x
    if tot % 3 != 0:
        print(0)
        return
    print(6)

t = 1
t = int(input())
for _ in range(t):
    solve()