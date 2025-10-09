class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def solve():
    n = int(input())
    freq = {}
    for _ in range(n):
        for word in input().split():
            word = word.lower()
            last = 0
            for i in range(len(word)):
                if not word[i].isalpha() and not word[i].isdigit():
                    xxx = word[last:i]
                    if len(xxx.strip()) > 0:
                        freq[xxx] = freq.get(xxx, 0) + 1
                    last = i + 1
            if last < len(word):
                xxx = word[last:]
                if len(xxx.strip()) > 0:
                    freq[xxx] = freq.get(xxx, 0) + 1
    a = []
    for key in freq:
        a.append(Pair(key, freq[key]))
    a.sort(key=lambda xx: (-xx.y, xx.x))
    for xx in a:
        print(xx.x, xx.y)

t = 1
# t = int(input())
for _ in range(t):
    solve()