def solve():
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(d, n):
        print(a[i], end = " ")
    for i in range(0, d):
        print(a[i], end = " ")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()