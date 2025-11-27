import math

def solve():
    s = input()
    n = len(s)
    i = 1
    j = n - 2
    while i < n:
        dist = abs(ord(s[i]) - ord(s[i - 1]))
        dist_reverse = abs(ord(s[j]) - ord(s[j + 1]))
        if dist != dist_reverse:
            print("NO")
            return
        i += 1
        j -= 1
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()