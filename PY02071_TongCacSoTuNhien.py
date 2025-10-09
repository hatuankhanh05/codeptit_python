res = []

def Try(n, maxVal, a):
    if n == 0:
        res.append(a.copy())
        return
    for i in range(min(n, maxVal), 0, -1):
        a.append(i)
        Try(n - i, i, a)
        a.pop()

def solve():
    n = int(input())
    res.clear()
    Try(n, n, [])
    print(len(res))
    for a in res:
        print("(" + " ".join(map(str, a)) + ")", end = " ")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()