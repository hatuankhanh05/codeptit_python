def solve():
    x = input()
    n = len(x)
    i = 0
    while i < n:
        c = x[i]
        j = i + 1
        m = 0
        while j < n and not x[j].isalpha():
            m = m * 10 + int(x[j])
            j += 1
        for _ in range(m):
            print(c, end="")
        i = j
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()