import math

is_prime = [True] * 1000001

def sieve():
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(1000000)) + 1):
        if is_prime[i] == True:
            for j in range(i * i, 1000000, i):
                is_prime[j] = False

def solve():
    n = int(input())
    res = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0 and is_prime[j]:
                if i // j != j and is_prime[i // j]:
                    res += 1
                else:
                    count = 0
                    while i % j == 0:
                        count += 1
                        i //= j
                    if count == 4 and i == 1:
                        res += 1
                break
    print(res)

sieve()
t = 1
# t = int(input())
for _ in range(t):
    solve()