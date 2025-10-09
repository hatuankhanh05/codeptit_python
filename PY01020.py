def solve():
    n = input()
    if len(n) < 2:
        print("NO")
        return
    if n[-2:] == "86":
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for _ in range(t):
    solve()