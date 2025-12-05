'''
    author: htkhanh05
    created at: 05.12.2025 17:52:14
'''

'''
HINT:
- Áp dụng công thức nội suy lagrange
'''

MOD = 10**9 + 7

def modPow(a, b):
    global MOD
    if b == 0:
        return 1
    if b % 2 == 0:
        c = modPow(a, b // 2) % MOD
        return c * c % MOD
    return a * modPow(a, b - 1)

# 1 / n mod M = n^-1 mod M = n^(MOD - 2) mod M
def inv(n):
    return modPow(n, MOD - 2)

def solve():
    global MOD
    n, k = map(int, input().split())
    d = k + 1
    if n <= d:
        ans = 0
        for i in range(1, n + 1):
            ans = (ans + modPow(i, k)) % MOD
        print(ans)
        return
    # Tính các điểm mẫu y[i]
    y = [0] * (d + 1)
    for i in range(1, d + 1):
        y[i] = (y[i - 1] + modPow(i, k)) % MOD
    fact = [1] * (d + 1)
    invFact = [1] * (d + 1)
    for i in range(1, d + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    invFact[d] = inv(fact[d])
    for i in range(d - 1, -1, -1):
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD
    # pre[i] là tích (n - 0) * (n - 1) ... (n - (i - 1))
    # suf[i] là tích (n - (i + 1)) * (n - (i + 2)) ... (n - d)
    pre = [1] * (d + 1)
    suf = [1] * (d + 1)
    for i in range(d):
        pre[i + 1] = pre[i] * (n - i) % MOD
    for i in range(d, 0, -1):
        suf[i - 1] = suf[i] * (n - i) % MOD
    ans = 0
    # tmp = (y[i] * nume * invDeno) % MOD
    for i in range(d + 1):
        nume = (pre[i] * suf[i]) % MOD
        invDeno = (invFact[i] * invFact[d - i]) % MOD
        tmp = (y[i] * nume) % MOD
        tmp = (tmp * invDeno) % MOD
        sign = 1
        if (d - i) % 2 != 0:
            sign = -1
        if sign == -1:
            ans = (ans - tmp + MOD) % MOD
        else:
            ans = (ans + tmp) % MOD
    print(ans)

if __name__ == '__main__':
    t = 1
    t = int(input())
    for _ in range(t):
        solve()