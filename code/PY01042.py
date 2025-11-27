def solve():
    num = input()
    for d in num:
        if d != '0' and d != '1' and d != '2':
            print("NO")
            return
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()