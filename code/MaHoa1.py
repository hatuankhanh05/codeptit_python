def solve():
    x = input()
    i = 0
    n = len(x)
    while i < n:
        c = x[i]
        j = i
        cnt = 0
        while j < n and x[j] == x[i]:
            cnt += 1
            j += 1
        print(f"{cnt}{c}", end="")
        i = j
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()