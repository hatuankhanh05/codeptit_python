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
    if not isPrime(len(num)):
        print("NO")
        return
    cnt_prime = 0
    cnt_nprime = 0
    for c in num:
        d = int(c)
        if d == 2 or d == 3 or d == 5 or d == 7:
            cnt_prime += 1
        else:
            cnt_nprime += 1
    print("YES" if cnt_prime > cnt_nprime else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()