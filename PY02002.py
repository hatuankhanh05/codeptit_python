import math

fibo_num = [0] * 93

def calFiboNum():
    fibo_num[1] = fibo_num[2] = 1
    for i in range(3, 93):
        fibo_num[i] = fibo_num[i - 1] + fibo_num[i - 2]

def solve():
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(fibo_num[i], end = " ")
    print()

t = 1
t = int(input())
calFiboNum()
for _ in range(t):
    solve()