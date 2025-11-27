import math

INF = 10 ** 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mx = [-INF, -INF, -INF]
    pos = [-1, -1, -1]
    for i in range(n):
        x = a[i]
        if x > mx[0]:
            mx[0] = x
            pos[0] = i
        
    tot = sum(mx)
    print(tot)

t = 1
t = int(input())
for _ in range(t):
    solve()