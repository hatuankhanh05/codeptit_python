def solve():
    n = int(input())
    x = [n - i for i in range(n)]
    res = []
    while True:
        res.append(''.join(map(str, x)))
        i = n - 2
        while i >= 0 and x[i] < x[i + 1]:
            i -= 1
        if i < 0:
            break
        j = n - 1
        while x[j] > x[i]:
            j -= 1
        x[i], x[j] = x[j], x[i]
        l = i + 1
        r = n - 1
        while l < r:
            x[l], x[r] = x[r], x[l]
            l += 1
            r -= 1
    print(len(res))
    for y in res:
        print(y, end = " ")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()