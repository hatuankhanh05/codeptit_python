def solve():
    s = input()
    mp = {}
    for i in range(0, len(s), 2):
        x = int(s[i:i + 2])
        if x < 10:
            continue
        mp[x] = mp.get(x, 0) + 1
    for x in mp:
        print(x, mp[x])

t = 1
# t = int(input())
for _ in range(t):
    solve()