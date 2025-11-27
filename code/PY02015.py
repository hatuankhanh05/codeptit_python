import math

def solve():
    while True:
        a = list(map(int, input().split()))
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
            break
        steps = 0
        while True:
            if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
                break
            b = []
            for i in range(0, 3):
                b.append(abs(a[i] - a[i + 1]))
            b.append(abs(a[0] - a[3]))
            a = list.copy(b)
            steps += 1
        print(steps)

t = 1
# t = int(input())
for _ in range(t):
    solve()