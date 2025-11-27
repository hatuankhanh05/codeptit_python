import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    freq = [0] * 1000001
    for x in a:
        freq[x] += 1
    choosen = -1
    max_freq = 0
    for x in a:
        if freq[x] <= n // 2:
            continue
        if freq[x] > max_freq:
            max_freq = freq[x]
            choosen = x
        elif freq[x] == max_freq:
            choosen = min(choosen, x)
    print(choosen if choosen != -1 else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()