import math

def productOfDigits(num):
    product = 1
    for d in num:
        if d == '0':
            continue
        product *= int(d)
    return product

def solve():
    num = input()
    print(productOfDigits(num))

t = 1
t = int(input())
for _ in range(t):
    solve()