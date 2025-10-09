import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def ok(num):
    for i in range(len(num)):
        if isPrime(i) ^ isPrime(int(num[i])):
            return False
    return True

def solve():
    num = input()
    print("YES" if ok(num) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()