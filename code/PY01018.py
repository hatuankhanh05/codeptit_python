p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

def solve():
    while 1:
        inp = input()
        if inp[0] == "0":
            break
        k, s = inp.split(" ")
        k = int(k)
        a = []
        for c in s:
            a.append(c)
        for i in range(len(a)):
            a[i] = p[(p.find(a[i]) + k) % 28]
        for i in range(len(a) - 1, -1, -1):
            print(a[i], end = "")
        print()

t = 1
# t = int(input())
for _ in range(t):
    solve()