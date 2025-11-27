def find(p, c):
    for i in range(len(p)):
        if c == p[i]: return i
    return -1

def solve():
    p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    while 1:
        inp = input().strip().split()
        if inp[0] == "0":
            break
        k = int(inp[0])
        s = inp[1]
        ans = ""
        for c in s:
            pos = find(p, c)
            ans = p[(pos + k) % 28] + ans
        print(ans)

t = 1
# t = int(input())
for _ in range(t):
    solve()