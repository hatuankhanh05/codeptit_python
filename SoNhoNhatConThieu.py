def solve():
    n = int(input())
    a = list(map(int, input().split()))
    freq = [0] * (3 * 10**4 + 1)
    for x in a:
        freq[x] += 1
    for i in range(1, n + 1):
        if freq[i] < 1:
            print(i)
            return
    print(n + 1)

t = 1
# t = int(input())
for _ in range(t):
    solve()