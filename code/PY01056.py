import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def ok(num):
    sum = 0
    for i in range(0, len(num), 2):
        d = int(num[i])
        if d % 2 != 0:
            return False
        sum += d
    for i in range(1, len(num), 2):
        d = int(num[i])
        if d % 2 == 0:
            return False
        sum += d
    return isPrime(sum)

def solve():
    num = input()
    print("YES" if ok(num) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()