def solve():
    s = input()
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            print("NO")
            return
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()