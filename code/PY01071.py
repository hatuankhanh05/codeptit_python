import math

def solve():
    s = input()
    if len(s) < 3:
        print("no")
        return
    if s[-3:].lower() == ".py":
        print("yes")
    else:
        print("no")

t = 1
# t = int(input())
for _ in range(t):
    solve()