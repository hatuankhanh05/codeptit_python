def bintodec(s):
    x = 0
    for c in s:
        x = x * 2 + int(c)
    return x

def solve():
    b = int(input())
    s = input()
    if(b == 2):
        print(s)
        return
    mp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    n = bintodec(s)
    a = []
    while n > 0:
        a.append(mp[n % b])
        n //= b
    for i in range(len(a) - 1, -1, -1):
        print(a[i], end = "")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()