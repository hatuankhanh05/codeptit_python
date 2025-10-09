import math
import bisect

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(0, n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            tot = a[i] + a[left] + a[right]
            if tot == 0:
                res += 1
                left += 1
            elif tot < 0:
                left += 1
            else:
                right -= 1
    print(res)

t = 1
t = int(input())
for _ in range(t):
    solve()