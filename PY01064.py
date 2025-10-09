import math

len = [0] * 26

def calLen():
    len[1] = 1
    for i in range(2, 26):
        len[i] = len[i - 1] * 2 + 1

def find(n, k):
    if n == 1:
        return 'A'
    if k == len[n - 1] + 1:
        return chr(ord('A') + n - 1)
    if k > len[n - 1] + 1:
        return find(n - 1, k - (len[n - 1] + 1))
    else:
        return find(n - 1, k)

def solve():
    n, k = map(int, input().split())
    print(find(n, k))

calLen()
t = 1
t = int(input())
for _ in range(t):
    solve()