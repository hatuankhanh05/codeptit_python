def solve():
    n = input()
    f = [0] * 10
    cnt = 0
    for x in n:
        d = ord(x) - ord('0')
        if f[d] == 0:
            cnt += 1
            if cnt > 2:
                print("NO")
                return
        f[d] += 1
    for i in range(2, len(n), 2):
        if n[i] != n[i - 2]:
            print("NO")
            return
    for i in range(3, len(n), 2):
        if n[i] != n[i - 2]:
            print("NO")
            return
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()