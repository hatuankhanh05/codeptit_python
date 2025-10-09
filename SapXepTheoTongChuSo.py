def sod(x):
    ans = 0
    while x:
        ans += x % 10
        x //= 10
    return ans

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: (sod(x), x))
    for x in a: print(x, end = " ")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()