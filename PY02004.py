import math

def solve():
    n = int(input())
    bits = list(map(int, input().split()))
    count_diff = 0
    for i in range(1, n):
        if bits[i] != bits[i - 1]:
            count_diff += 1
    print(count_diff)

t = 1
# t = int(input())
for _ in range(t):
    solve()