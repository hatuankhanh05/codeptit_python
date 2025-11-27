import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def solve():
    num = input()
    n = len(num)
    print("YES" if isPrime(int(num[0:3])) and isPrime(int(num[-3:])) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()