def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    cnt = 0
    lack = []
    for i in range(n):
        if a[i] <= b[i]:
            res += a[i]
            cnt += 1
        else:
            res += b[i]
            lack.append(a[i] - b[i])
    lack.sort()
    if cnt < k:
        res += sum(lack[:k - cnt])
    print(res)
            
t = 1
# t = int(input())
for _ in range(t):
    solve()