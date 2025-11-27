import math

def solve():
    num = input()
    n = len(num)
    sum = 0
    product = 1
    cnt = 0
    for i in range(n):
        d = int(num[i])
        if i % 2 == 0:
            if d == 0:
                continue
            product *= d
            cnt += 1
        else:
            sum += d
    if not cnt:
        product = 0
    print(product, sum)


t = 1
t = int(input())
for _ in range(t):
    solve()