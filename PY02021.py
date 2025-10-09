def solve():
    n, m, o = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    i, j, k = 0, 0, 0
    res = []
    while i < n and j < m and k < o:
        if a[i] == b[j] and a[i] == c[k]:
            res.append(a[i])
            i += 1
            j += 1
            k += 1
        elif a[i] > b[j]:
            j += 1
        elif a[i] > c[k]:
            k += 1
        else:
            i += 1
    if len(res) > 0:
        for x in res:
            print(x, end = " ")
        print()
    else:
        print("NO")
    

t = 1
t = int(input())
for _ in range(t):
    solve()