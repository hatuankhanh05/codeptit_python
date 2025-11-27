def hanoiTower(n, source, auxiliary, target):
    if n == 1:
        print(source + " -> " + target)
        return
    hanoiTower(n - 1, source, target, auxiliary)
    print(source + " -> " + target)
    hanoiTower(n - 1, auxiliary, source, target)

def solve():
    n = int(input())
    hanoiTower(n, 'A', 'B', 'C')

t = 1
# t = int(input())
for _ in range(t):
    solve()