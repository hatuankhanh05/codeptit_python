def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def solve():
    n, k = map(int, input().split())
    min = 1
    max = 1
    for i in range(k - 1):
        min *= 10
    for i in range(k):
        max *= 10
    cnt = 0
    for i in range(min, max):
        if gcd(n, i) == 1:
            print(i, end = " ")
            cnt += 1
            if cnt == 10:
                cnt = 0
                print()

t = 1
# t = int(input())
for _ in range(t):
    solve()