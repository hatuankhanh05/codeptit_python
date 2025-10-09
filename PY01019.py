import math

def solve():
    s = input()
    left = 1
    right = len(s) - 2
    ok = 1
    while left < len(s):
        if abs(ord(s[left]) - ord(s[left - 1])) != abs(ord(s[right]) - ord(s[right + 1])):
            ok = 0
            break
        left += 1
        right -= 1
    print("YES" if ok else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()