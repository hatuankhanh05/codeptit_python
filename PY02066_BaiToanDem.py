from sys import stdin

def solve():
    n = int(input())
    lines = stdin.read()
    a = list(map(int, lines.split()))
    has = [0] * 201
    mx = max(a)
    for i in range(n):
        has[a[i]] = 1
    isExcel = 1
    for i in range(1, mx + 1):
        if has[i] == 0:
            print(i)
            isExcel = 0
    if isExcel == 1:
        print("Excellent!")

t = 1
# t = int(input())
for _ in range(t):
    solve()