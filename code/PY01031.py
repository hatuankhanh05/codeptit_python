import math

rs = []

def calR():
    for i in range(10):
        rs.append(i)
    for i in range(26):
        rs.append(chr(i + ord('A')))

def solve():
    n, b = map(int, input().split())
    a = []
    while n > 0:
        r = n % b
        a.append(rs[r])
        n //= b
    a.reverse()
    for x in a:
        print(x, end = "")
    print()

calR()
t = 1
t = int(input())
for _ in range(t):
    solve()