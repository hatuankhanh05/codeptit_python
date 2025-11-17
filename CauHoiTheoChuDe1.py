import sys

n = int(input())
lines = sys.stdin.readlines()
isTheme = True
quiz = {}
curTheme = ''

for line in lines:
    if isTheme:
        curTheme = line.replace('\n', '')
        quiz[curTheme] = 0
        isTheme = False
        continue
    if not line.strip():
        isTheme = True
        continue
    quiz[curTheme] += 1

for x in quiz:
    print(f"{x}: {quiz[x]}")