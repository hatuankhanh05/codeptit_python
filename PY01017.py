def solve():
    s = input()
    i = 0
    n = len(s)
    while i < n:
        j = i
        cnt = 0
        while j < n and s[j] == s[i]:
            cnt += 1
            j += 1
        print(str(cnt) + s[i], end = "")
        i = j
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()