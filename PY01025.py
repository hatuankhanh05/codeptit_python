def solve():
    s = input()
    comma = [0] * len(s)
    cnt = 0
    for i in range(len(s) - 1, -1, -1):
        cnt += 1
        if cnt == 3:
            cnt = 0
            comma[i] = 1
    for i in range(len(s)):
        if comma[i] and i != 0:
            print(",", end = "")
        print(s[i], end = "")

t = 1
# t = int(input())
for _ in range(t):
    solve()