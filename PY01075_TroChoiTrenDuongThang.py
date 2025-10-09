import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    mp = {0: 0}
    g_arr = [0]
    for i in range(n):
        for g in g_arr:
            new_g = math.gcd(a[i], g)
            new_cost = mp[g] + c[i]
            if new_g not in g_arr:
                g_arr.append(new_g)
                mp[new_g] = new_cost
            elif new_cost < mp[new_g]:
                mp[new_g] = new_cost
    print(-1 if 1 not in mp else mp[1])

t = 1
t = int(input())
for _ in range(t):
    solve()