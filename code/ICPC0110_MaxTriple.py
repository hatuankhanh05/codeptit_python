def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        return
    if n == 2:
        print(a[0] + a[1])
        return
    mx = [- 10 ** 8 - 1] * 3
    pos = [-1] * 2
    for i in range(n):
        if a[i] > mx[0]:
            mx[0] = a[i]
            pos[0] = i
    for i in range(n):
        if i == pos[0]:
            continue
        if a[i] > mx[1]:
            mx[1] = a[i]
            pos[1] = i
    for i in range(n):
        if i == pos[0] or i == pos[1]:
            continue
        if a[i] > mx[2]:
            mx[2] = a[i]
    print(mx[0] + mx[1] + mx[2])

t = 1
t = int(input())
for _ in range(t):
    solve()