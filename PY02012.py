def solve():
    n = int(input())
    a = list(map(int, input().split()))
    evens = [x for x in a if x % 2 == 0]
    odds = [x for x in a if x % 2 != 0]
    evens.sort()
    odds.sort(reverse = True)
    ie = 0
    io = 0
    for x in a:
        if x % 2 == 0 and ie < len(evens):
            print(evens[ie], end = " ")
            ie += 1
        elif x % 2 != 0 and io < len(odds):
            print(odds[io], end = " ")
            io += 1

t = 1
# t = int(input())
for _ in range(t):
    solve()