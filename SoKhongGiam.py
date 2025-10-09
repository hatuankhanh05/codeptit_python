def solve():
    x = input()
    n = len(x)
    for i in range(n - 1):
        if x[i] > x[i + 1]:
            print("NO")
            return
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()