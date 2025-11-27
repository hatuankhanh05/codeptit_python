import math

# tất cả số nguyên tố <= 50
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def count_divisible(L, R, primes):
    res = 0
    m = len(primes)
    for mask in range(1, 1 << m):
        lcm = 1
        bits = 0
        valid = True
        for i in range(m):
            if mask >> i & 1:
                bits += 1
                g = math.gcd(lcm, primes[i])
                lcm = lcm // g * primes[i]
                if lcm > R:   # không cần xét nữa
                    valid = False
                    break
        if not valid:
            continue
        cnt = R // lcm - (L - 1) // lcm
        if bits % 2 == 1:
            res += cnt
        else:
            res -= cnt
    return res

def solve():
    while True:
        line = input().strip()
        if line == "-1":
            break
        L, R = map(int, line.split())
        N = int(input())
        primes = [p for p in PRIMES if p <= N]
        total = R - L + 1
        bad = count_divisible(L, R, primes)
        print(total - bad)

if __name__ == "__main__":
    solve()
