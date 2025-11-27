import math

def solve():
    s1 = input()
    s2 = input()
    a = []
    b = []
    for ch in s2:
        a.append(ch)
    for ch in s1:
        b.append(ch)
    a.sort()
    b.sort()
    s2 = "".join(a)
    s1 = "".join(b)
    if s1 == s2:
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for _ in range(t):
    print("Test " + str(_ + 1) + ": ", end = "")
    solve()