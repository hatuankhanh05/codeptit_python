def solve():
    a, k, n = map(int, input().split())
    ans = []
    for total in range(0, n + 1, k):
        if total > a:
            ans.append(total - a)
    if not len(ans):
        print(-1)
        return
    for x in ans:
        print(x, end = " ")
    print()

t = 1
# t = int(input())
for _ in range(t):
    solve()