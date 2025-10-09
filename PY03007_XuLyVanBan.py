import sys

def solve():
    words = sys.stdin.read().strip().split()
    sentence = []
    first = True
    for word in words:
        if first:
            word = word.capitalize()
            first = False
        else:
            word = word.lower()
        if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
            first = True
            word = word[:-1]
        sentence.append(word)
        if first:
            print(' '.join(sentence))
            sentence.clear()

t = 1
# t = int(input())
for _ in range(t):
    solve()