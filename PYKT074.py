import math

def solve():
    s = input()
    a = s.split()
    cnt = 0
    for i in range(len(a)):
        x = a[i]
        if cnt + len(x) > 100:
            break
        cnt += len(x)
        if i != len(a) - 1:
            cnt += 1
        print(x, end = " ")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()