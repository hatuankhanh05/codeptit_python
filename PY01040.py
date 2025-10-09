import math

def rot(a):
    tot = sum(ord(ch) - ord('A') for ch in a)
    for i in range(len(a)):
        a[i] = chr((ord(a[i]) + tot) % 26 + ord('A'))
    return a

def solve():
    s = input()
    a = [ch for ch in s[0 : len(s) // 2]]
    b = [ch for ch in s[len(s) // 2 :]]
    a = rot(a)
    b = rot(b)
    for i in range(len(a)):
        a[i] = chr((ord(a[i]) - ord('A') + ord(b[i]) - ord('A')) % 26 + ord('A'))
    for x in a:
        print(x, end = "")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()