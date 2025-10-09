import math

def solve():
    n = int(input())
    freq = [0] * 1001
    for i in range(n):
        x = int(input())
        freq[x] += 1
    choosen = 0
    max_freq = 0
    for i in range(1, 1001):
        if freq[i] > max_freq:
            max_freq = freq[i]
            choosen = i
    print(choosen)

t = 1
t = int(input())
for _ in range(t):
    solve()