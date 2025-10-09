import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            return
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()