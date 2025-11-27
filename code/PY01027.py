import math 

def solve():
    s = input()
    i = 0
    while i < len(s):
        sub3 = s[i:i + 3]
        if sub3 == "688":
            i += 3
            continue
        sub2 = s[i:i + 2]
        if sub2 == "68":
            i += 2
            continue
        if s[i] != '6':
            print("NO")
            return
        i += 1
    print("YES")

t = 1
# t = int(input())
for _ in range(t):
    solve()