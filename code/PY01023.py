import math

def solve():
    n = int(input())
    print("1 * ", end = "")
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            print(str(i) + "^" + str(cnt), end = "")
            if n != 1:
                print(" * ", end = "")
    if n != 1:
        print(str(n) + "^" + str(1), end = "")
    print()

t = 1
t = int(input())
for _ in range(t):
    solve()