import math

def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        se = {0}
        while True:
            se.add(n)
            if n == 1:
                break
            if n % 2 == 0:
                n //= 2
            else:
                n = n * 3 + 1
        print(len(se) - 1)

t = 1
# t = int(input())
for _ in range(t):
    solve()