def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def solve():
    l, r = map(int, input().split())
    for i in range(l, r - 1):
        for j in range(i + 1, r):
            if gcd(i, j) != 1:
                continue
            for k in range(j + 1, r + 1):
                if gcd(i, k) == 1 and gcd(j, k) == 1:
                    print("(" + str(i) + ", " + str(j) + ", " + str(k) + ")")

t = 1
# t = int(input())
for _ in range(t):
    solve()