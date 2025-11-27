def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = set(a)
    b = set(b)
    a = sorted(list(a))
    b = sorted(list(b))
    if len(a) != len(b):
        print("NO")
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                print("NO")
                return
        print("YES")

t = 1
# t = int(input())
for _ in range(t):
    solve()