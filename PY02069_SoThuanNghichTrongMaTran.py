def isPalin(x):
    y = x
    z = 0
    cnt = 0
    while x > 0:
        z = z * 10 + x % 10
        x //= 10
        cnt += 1
    return cnt >= 2 and z == y

def solve():
    n, m = map(int, input().split())
    a = [[] for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    maxPalin = -1
    for i in range(n):
        for j in range(m):
            if isPalin(a[i][j]):
                maxPalin = (max(maxPalin, a[i][j]) if maxPalin != -1 else a[i][j])
    if maxPalin == -1:
        print("NOT FOUND")
        return
    print(maxPalin)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxPalin:
                print("Vi tri " + "[" + str(i) + "]" + "[" + str(j) + "]")

t = 1
# t = int(input())
for _ in range(t):
    solve()