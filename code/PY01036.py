def solve():
    n = int(input())
    res = 0
    start = 1 if n % 2 != 0 else 2
    for i in range(start, n + 1, 2):
        res += 1 / i
    print("{:.6f}".format(res))

t = 1
t = int(input())
for _ in range(t):
    solve()