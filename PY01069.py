import itertools

def solve():
    n = int(input())
    d = ['2', '3', '5', '7']
    se = set(d)
    res = []
    for length in range(4, n + 1):
        for comb in itertools.product(d, repeat = length):
            if set(comb) >= se and comb[-1] != "2":
                res.append(int("".join(comb)))
    res.sort()
    for x in res:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()