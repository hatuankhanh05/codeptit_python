def solve():
    s = input()
    sod = 0
    for c in s:
        sod += int(c)
    if sod % 10 != 0:
        print("NO")
        return
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != 2:
            print("NO")
            return
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()