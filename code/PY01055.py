import math

def ok(num):
    if len(num) == 1:
        return True
    if len(num) % 2 == 0:
        return False
    if num[0] == num[1]:
        return False
    for i in range(2, len(num), 2):
        if num[i] != num[i - 2]:
            return False
    return True

def solve():
    num = input()
    print("YES" if ok(num) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()