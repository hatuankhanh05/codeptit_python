import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    num = input()
    if not isPrime(len(num)):
        print("NO")
        return
    cnt = 0
    for c in num:
        d = int(c)
        if isPrime(d):
            cnt += 1
    print("YES" if cnt > len(num) - cnt else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()