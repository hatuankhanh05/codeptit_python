import math

is_prime = [1] * 1000001
def sieve():
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(math.sqrt(1e6 + 1))):
        if is_prime[i]:
            for j in range(i * i, int(1e6 + 1), i):
                is_prime[j] = 0

def rev(n):
    m = 0
    while n:
        m = m * 10 + n % 10
        n //= 10
    return m

def solve():
    n = int(input())
    used = [0] * int(1e6)
    for i in range(n):
        j = rev(i)
        if(j >= n):
            continue
        if i == rev(i):
            continue
        if used[i]:
            continue
        if is_prime[i] and is_prime[j]:
            print(i, j, end = " ")
            used[i] = 1
            used[j] = 1
    print()

sieve()
t = 1
t = int(input())
for _ in range(t):
    solve()