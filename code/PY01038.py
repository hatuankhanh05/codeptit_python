def reverse(n):
    m = 0
    while n > 0:
        m = m * 10 + n % 10
        n //= 10
    return m

def solve():
    n = int(input())
    for i in range(1000):
        if n % 7 == 0:
            print(n)
            return
        n += reverse(n)
    print(-1)

t = 1
t = int(input())
for _ in range(t):
    solve()