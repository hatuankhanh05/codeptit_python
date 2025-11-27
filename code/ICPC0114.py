import math

def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n + 1))):
        if n % i == 0:
            return 0
    return 1

def rev_check(n):
    m = 0
    while n:
        m = m * 10 + n % 10
        n //= 10
    return is_prime(m)

def sod_check(n):
    sum = 0
    while n:
        d = n % 10
        if not is_prime(d):
            return 0
        sum += d
        n //= 10
    return is_prime(sum)

def solve():
    n = int(input())
    if is_prime(n) and rev_check(n) and sod_check(n):
        print("Yes")
    else:
        print("No")

t = 1
t = int(input())
for _ in range(t):
    solve()