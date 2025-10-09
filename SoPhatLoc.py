def solve():
    x = input()
    if len(x) > 1 and x[-2:] == "86":
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for _ in range(t):
    solve()