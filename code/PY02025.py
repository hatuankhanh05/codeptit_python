def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sa = set(a)
    sb = set(b)
    a = sorted(list(sa))
    b = sorted(list(sb))
    freq = [0] * 10001
    fb = [0] * 10001
    for x in a:
        freq[x] = 1
    for x in b:
        fb[x] = 1
    for x in b:
        if freq[x] > 0:
            print(x, end = " ")
    print()
    for x in a:
        if fb[x] < 1:
            print(x, end = " ")
    print()
    for x in b:
        if freq[x] < 1:
            print(x, end = " ")

t = 1
# t = int(input())
for _ in range(t):
    solve()