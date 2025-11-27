def solve():
    n = int(input())
    freq = {}
    for x in list(map(int, input().split())):
        freq[x] = freq.get(x, 0) + 1
    for key in freq.keys():
        if freq[key] % 2 != 0:
            print(key)
            return

t = 1
t = int(input())
for _ in range(t):
    solve()