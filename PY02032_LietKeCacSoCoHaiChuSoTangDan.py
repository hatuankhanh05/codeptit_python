def solve():
    Str = input()
    s = {0}
    for i in range(0, len(Str), 2):
        x = int(Str[i:i + 2])
        if x < 10:
            continue
        s.add(x)
    a = list(s)
    a.sort()
    for i in range(1, len(a)):
        print(a[i], end = " ")

t = 1
# t = int(input())
for _ in range(t):
    solve()