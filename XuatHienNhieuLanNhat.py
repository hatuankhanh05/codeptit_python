def solve():
    n = int(input())
    a = list(map(int, input().split()))
    freq = [0] * (10**6 + 1)
    for x in a:
        freq[x] += 1
    ans = -1
    mx = 0
    for x in a:
        if freq[x] > n / 2:
            if freq[x] > mx:
                ans = x
                mx = freq[x]
            elif freq[x] == mx and x < ans:
                ans = x
    print("NO" if ans == -1 else ans)

t = 1
t = int(input())
for _ in range(t):
    solve()