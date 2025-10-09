def solve():
    n = input()
    a = []
    for d in n:
        a.append(int(d))
    for i in range(len(n) - 1, 0, -1):
        if a[i] >= 5:
            a[i] = 0
            a[i - 1] += 1
        else:
            a[i] = 0
    for x in a:
        print(x, end = "")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()