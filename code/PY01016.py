def solve():
    s = input()
    for i in range(0, len(s), 2):
        times = int(s[i + 1])
        while times:
            print(s[i], end = "")
            times -= 1
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()