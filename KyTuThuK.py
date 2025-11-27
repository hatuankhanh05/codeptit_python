'''
    author: htkhanh05
    created at: 27.11.2025 13:00:59
'''
length = [0] * 26

def preCal():
    for i in range(1, 26):
        length[i] = length[i - 1] * 2 + 1

def find(n, k):
    if k == length[n - 1] + 1:
        return n
    if k <= length[n - 1]:
        return find(n - 1, k)
    return find(n - 1, k - 1 - length[n - 1])

def solve():
    n, k = map(int, input().split())
    print(chr(ord('A') + find(n, k) - 1))

t = 1
preCal()
t = int(input())
for _ in range(t):
    solve()