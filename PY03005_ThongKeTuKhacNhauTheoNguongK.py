def solve():
    n, k = map(int, input().split())
    mp = {}
    for _ in range(n):
        s = input().split()
        for word in s:
            word = word.lower()
            word = word
            last = 0
            for i in range(len(word)):
                if not word[i].isdigit() and not word[i].isalpha():
                    x = word[last:i]
                    last = i + 1
                    if len(x.strip()) > 0:
                        mp[x] = mp.get(x, 0) + 1
            if last < len(word):
                x = word[last:]
                if len(x.strip()) > 0:
                    mp[x] = mp.get(x, 0) + 1
    a = []
    for key in mp:
        if mp[key] >= k:
            a.append((key, mp[key]))
    a.sort(key=lambda x: (-x[1], x[0]))
    for (key, val) in a:
        print(key, val)

t = 1
# t = int(input())
for _ in range(t):
    solve()