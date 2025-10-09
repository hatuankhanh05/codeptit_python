import math

def solve():
    p, q = map(str, input().split())
    x1 = input().strip()
    if len(x1.split()) > 1:
        x1, x2 = map(str, x1.split())
    else:
        x2 = input()
    if int(p) > int(q):
        p, q = q, p
    print(int(x1.replace(q, p)) + int(x2.replace(q, p)), end = " ")
    print(int(x1.replace(p, q)) + int(x2.replace(p, q)))

t = 1
t = int(input())
for _ in range(t):
    solve()