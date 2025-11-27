def solve():
    n = int(input())
    a = list(map(int, input().split()))
    minSteps = 10 ** 9
    chosenVal = -1
    for i in range(n):
        tot = 0
        for j in range(n):
            if j == i:
                continue
            tot += abs(a[j] - a[i])
        if tot < minSteps:
            minSteps = tot
            chosenVal = a[i]
    print(minSteps, chosenVal)

t = 1
# t = int(input())
for _ in range(t):
    solve()