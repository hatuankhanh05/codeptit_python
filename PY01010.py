def solve():
    n = input()
    if n[0:2] == n[-2:]:
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for _ in range(t):
    solve()