def solve():
    n = int(input())
    u = float(input())
    p = list(map(float, input().split()))
    p.sort()
    while u > 0:
        allEqual = True
        for i in range(n - 1):
            if p[i] < p[i + 1]:
                allEqual = False
                bound = p[i + 1]
                need = (bound - p[i]) * (i + 1)
                if need <= u:
                    for j in range(i + 1):
                        p[j] = bound
                    u -= need
                else:
                    inc = u / (i + 1)
                    for j in range(i + 1):
                        p[j] += inc
                    u = 0
                    break
        if allEqual:
            inc = u / n
            for i in range(n):
                p[i] = min(1.0, p[i] + inc)
            u = 0
    res = 1.0
    for i in range(n):
        res *= p[i]
    print(f"{res:.6f}")
    

t = 1
t = int(input())
for _ in range(t):
    solve()