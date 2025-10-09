def solve():
    n = int(input())
    mp = {}
    for i in range(n):
        for word in input().strip().split():
            word = word.lower()
            last = 0
            for i in range(len(word)):
                if not word[i].isalnum():
                    chosenWord = word[last:i]
                    last = i + 1
                    validWord = ''.join([ch for ch in chosenWord if ch.isalpha()])
                    if validWord:
                        mp[validWord] = mp.get(validWord, 0) + 1
            if last < len(word):
                chosenWord = word[last:]
                validWord = ''.join([ch for ch in chosenWord if ch.isalpha()])
                if validWord:
                    mp[validWord] = mp.get(validWord, 0) + 1
    a = []
    for key in mp:
        a.append((key, mp[key]))
    a.sort(key=lambda x: (-x[1], x[0]))
    for (key, val) in a:
        print(key, val)

t = 1
# t = int(input())
for _ in range(t):
    solve()