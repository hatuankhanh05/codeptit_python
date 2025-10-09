def solve():
    n = int(input())
    a = list(map(int, input().split()))
    odds = []
    for x in a:
        if x % 2 != 0:
            odds.append(x)
    evens = []
    for x in a:
        if x % 2 == 0:
            evens.append(x)
    odds.sort(reverse = True)
    evens.sort()
    i = 0
    j = 0
    for idx in range(n):
        x = a[idx]
        if x % 2 == 0 and j < len(evens):
            print(evens[j], end = " ")
            j += 1
        elif x % 2 != 0 and i < len(odds):
            print(odds[i], end = " ")
            i += 1
        # if idx != n - 1:
        #     print(end = " ")

t = 1
# t = int(input())
for _ in range(t):
    solve()