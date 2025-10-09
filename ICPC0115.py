fact = [-1] * 10
def cal_fact():
    fact[0] = fact[1] = 1
    for i in range(2, 10):
        fact[i] = fact[i - 1] * i

def solve():
    n = int(input())
    m = n
    sum = 0
    while m:
        sum += fact[m % 10]
        m //= 10
    print("Yes" if n == sum else "No")

cal_fact()
t = 1
t = int(input())
for _ in range(t):
    solve()