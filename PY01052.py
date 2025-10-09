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
    sum_of_digits = 0
    for digit in num:
        sum_of_digits += int(digit)
    print("YES" if isPrime(sum_of_digits) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()