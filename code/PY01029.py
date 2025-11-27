def rev(n):
    m = 0
    while n > 0:
        m = m * 10 + n % 10
        n //= 10
    return m

def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def solve():
    n = int(input())
    m = rev(n)
    print("YES" if gcd(n, m) == 1 else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()