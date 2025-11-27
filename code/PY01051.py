import math

def isPalindrome(num):
    if len(num) < 2:
        return False
    for i in range(len(num)):
        if num[i] != num[len(num) - 1 - i]:
            return False
    return True

def solve():
    num = input()
    sum_of_digits = 0
    for c in num:
        d = int(c)
        sum_of_digits += d
    print("YES" if isPalindrome(str(sum_of_digits)) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()