def solve():
    s = input()
    k = int(input())
    mp = {}
    for i in range(0, len(s), 2):
        x = int(s[i:i + 2])
        if x < 10:
            continue
        mp[x] = mp.get(x, 0) + 1
    keys = [x for x in mp if mp[x] >= k]
    if len(keys) < 1:
        print("NOT FOUND")
        return
    keys.sort()
    for key in keys:
        print(key, mp[key])

t = 1
# t = int(input())
for _ in range(t):
    solve()