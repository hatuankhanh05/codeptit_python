def solve():
    n = input()
    if len(n) < 3:
        print("NO")
        return
    i = 1
    while i < len(n) and n[i] > n[i - 1]:
        i += 1
    if i == n:
        print("NO")
        return
    for j in range(i + 1, len(n)):
        if n[j] > n[j - 1]:
            print("NO")
            return
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()