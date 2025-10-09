import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def solve():
    num = input()
    if len(num) < 4:
        print("YEs" if isPrime(int(num)) else "NO")
        return
    print("YES" if isPrime(int(num[-4:])) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()