import math

def solve():
    s1 = input()
    s2 = input()
    p = int(input())
    i = 0
    while i < p - 1:
        print(s1[i], end = "")
        i += 1
    print(s2, end = "")
    while i < len(s1):
        print(s1[i], end = "")
        i += 1

t = 1
# t = int(input())
for _ in range(t):
    solve()