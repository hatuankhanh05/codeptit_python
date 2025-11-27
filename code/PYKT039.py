import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ok = True
    for i in range(n):
        if a[i] > b[i]:
            ok = False
            break
    print("YES" if ok else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()