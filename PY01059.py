import math

def solve():
    num = input()
    sum = 0
    product = 1
    cnt = 0
    for i in range(len(num)):
        d = int(num[i])
        if i % 2 == 0:
            sum += d
        else:
            if d == 0:
                continue
            product *= d
            cnt += 1
    product = 0 if not cnt else product
    print(sum, product)

t = 1
t = int(input())
for _ in range(t):
    solve()