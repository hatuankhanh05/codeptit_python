import math

def solve():
    n, x, m = map(float, input().split())
    ans = math.log(m / n) / math.log(1 + x / 100)
    print(math.ceil(ans))

t = 1
t = int(input())
for _ in range(t):
    solve()