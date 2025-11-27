import math

a = []

def calBase():
    global a
    for i in range(10):
        a.append(str(i))
    for i in range(26):
        a.append(chr(i + ord('A')))

def solve():
    n, b = map(int, input().split())
    c = []
    while n > 0:
        c.append(a[n % b])
        n //= b
    for i in range(len(c) - 1, -1, -1):
        print(c[i], end = "")
    print()

t = 1
t = int(input())
calBase()
for _ in range(t):
    solve()