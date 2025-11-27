import math

is_prime = [1] * 1000001
def sieve():
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(math.sqrt(1000001)) + 1):
        if is_prime[i]:
            for j in range(i * i, 1000001, i):
                is_prime[j] = 0

def solve():
    n = int(input())
    cnt = 0
    for i in range(n):
        if not is_prime[i]:
            continue
        if is_prime[i + 2] and is_prime[i + 6] and i + 2 <= n and i + 6 <= n:
            cnt += 1
        if is_prime[i + 4] and is_prime[i + 6] and i + 4 <= n and i + 6 <= n:
            cnt += 1
    print(cnt)

sieve()
t = 1
t = int(input())
for _ in range(t):
    solve()