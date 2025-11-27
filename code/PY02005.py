import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count_pair = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[j] < a[i]:
                count_pair += 1
    print(count_pair)

t = 1
# t = int(input())
for _ in range(t):
    solve()