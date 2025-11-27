import math

def solve():
    n = int(input())
    a = list(map(float, input().split()))
    a.sort()
    left = 0
    while left < n and a[left] == a[0]:
        left += 1
    right = n - 1
    while right >= 0 and a[right] == a[n - 1]:
        right -= 1
    total = 0
    count = 0
    for i in range(left, right + 1):
            total += a[i]
            count += 1
    res = total / count
    print("{:.2f}".format(res))

t = 1
# t = int(input())
for _ in range(t):
    solve()