def solve():
    n = int(input())
    cnt4, cnt7 = 0, 0
    while n:
        d = n % 10
        if d == 4:
            cnt4 += 1
        elif d == 7:
            cnt7 += 1
        n //= 10
    print("YES" if cnt4 + cnt7 == 4 or cnt4 + cnt7 == 7 else "NO")

t = 1
# t = int(input())
for _ in range(t):
    solve()