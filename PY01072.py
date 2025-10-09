import math

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    freq = [0] * 1001
    a_unique = []
    for x in a:
        if freq[x] < 1:
            a_unique.append(x)
        freq[x] += 1
    a_unique.sort()
    n = len(a_unique)
    b = [0] * k
    if k > n:
        for x in a_unique:
            print(x, end = " ")
        print()
        return
    for i in range(k):
        b[i] = i
    while True:
        for x in b:
            print(a_unique[x], end = " ")
        print()
        i = k - 1
        while i >= 0 and b[i] == n - k + i:
            i -= 1
        if i < 0:
            break
        b[i] += 1
        for j in range(i + 1, k):
            b[j] = b[j - 1] + 1

t = 1
# t = int(input())
for _ in range(t):
    solve()