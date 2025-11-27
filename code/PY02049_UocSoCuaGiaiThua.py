def solve():
    n, p = map(int, input().split())
    cnt = 0
    while n > 0:
        cnt += n // p
        n //= p
    print(cnt)

t = 1
t = int(input())
for _ in range(t):
    solve()