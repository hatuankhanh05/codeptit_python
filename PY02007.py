import sys

data = sys.stdin.read().splitlines()
count_unique = 0
freq = [0] * 42
for line in data:
    a = list(map(int, line.split()))
    for x in a:
        x %= 42
        if freq[x] < 1:
            count_unique += 1
        freq[x] += 1
print(count_unique)