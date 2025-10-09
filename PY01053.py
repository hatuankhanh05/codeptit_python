import math

def isDivisibleBy3(num):
    sum_of_digits = 0
    for d in num:
        sum_of_digits += int(d)
    return sum_of_digits % 3 == 0

def solve():
    num = input()
    print("YES" if isDivisibleBy3(num) else "NO")

t = 1
t = int(input())
for _ in range(t):
    solve()