import math

def solve():
    s = input()
    if s[0] == "." or s[-1] == ".":
        print("NO")
        return
    a = s.split(".")
    if len(a) != 4:
        print("NO")
        return
    for x in a:
        if not x.isdigit():
            print("NO")
            return
        temp = int(x)
        if temp < 0 or temp > 255:
            print("NO") 
            return
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()