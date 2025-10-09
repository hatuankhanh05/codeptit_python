import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    num = input()
    if len(num) < 4:
        print("YES" if isPrime(int(num)) else "NO")
        return
    print("YES" if isPrime(int(num[-4:])) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()