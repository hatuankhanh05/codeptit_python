def solve():
    n = input()
    for d in n:
        if d == '4' or d == '7':
            continue
        print("NO")
        return
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()