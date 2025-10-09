def solve():
    x = input().strip()
    y = x[::-1]
    n = len(x)
    for i in range(n - 1):
        val1 = abs(ord(x[i]) - ord(x[i + 1]))
        val2 = abs(ord(y[i]) - ord(y[i + 1]))
        if val1 != val2:
            print("NO")
            return
    print("YES")

t = 1
t = int(input())
for _ in range(t):
    solve()