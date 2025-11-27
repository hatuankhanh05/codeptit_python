from math import sqrt

n = int(input())

def check(x):
    cntPrime = 0
    ans = 1
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            cnt = 0
            while x % i == 0:
                cnt += 1
                x //= i
            ans *= cnt + 1
            cntPrime += 1
    if x > 1:
        cntPrime += 1
        ans *= 2
    return (cntPrime == 2 and ans == 4) or (cntPrime == 1 and ans == 5)

ans = 0
for i in range(2, int(sqrt(n)) + 1):
    if check(i) and i * i <= n:
        ans += 1
print(ans)