def solve():
    n = int(input())
    A = list(map(int, input().split()))
    L = min(A)
    R = max(A)
    mp = [False] * (R + 1)
    for x in A:
        mp[x] = True
    cnt = 0
    for i in range(L, R + 1):
        if not mp[i]:
            cnt += 1
    print(cnt)

T = int(input())
for _ in range(T):
    solve()