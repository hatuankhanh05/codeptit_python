import math
from itertools import permutations

def solve():
    s = input()
    for p in permutations(s):
        print("".join(p))

t = 1
# t = int(input())
for _ in range(t):
    solve()