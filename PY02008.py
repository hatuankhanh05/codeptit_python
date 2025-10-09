import math

MAX = 1000000
is_prime = [True] * (MAX + 1)
prime = []

def sieve():
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(MAX)) + 1):
        if is_prime[i] == True:
            for j in range(i * i, MAX + 1, i):
                is_prime[j] = False

def calPrime():
    for i in range(1, 1000000)                :
        if is_prime[i] == True:
            prime.append(i)
            if len(prime) == 1000:
                break

def solve():
    n, x = map(int, input().split())
    print(x, end = " ")
    for i in range(n):
        x += prime[i]
        print(x, end = " ")

t = 1
sieve()
calPrime()
# t = int(input())
for _ in range(t):
    solve()