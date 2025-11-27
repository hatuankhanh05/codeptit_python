import math

def solve():
    s = input()
    n = input()
    n_length = len(n)
    count = 0
    i = 0
    while i < len(s) - n_length + 1:
        if s[i:i + n_length] == n:
            count += 1
            i = i + n_length - 1
        i += 1
    print(count)

t = 1
t = int(input())
for _ in range(t):
    solve()