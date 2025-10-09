import math

x = [0] * 13
n = 0
res = []

def ok(k):
    cnt = [0] * 3
    for i in range(1, k + 1):
        cnt[x[i]] += 1
    return cnt[0] <= cnt[1] and cnt[1] <= cnt[2] and cnt[0] and cnt[1] and cnt[2]

def storeString(k):
    tmp_string = ""
    for i in range(1, k + 1):
        tmp_string += chr(x[i] + ord('A'))
    res.append(tmp_string)

def Try(i):
    for j in range(3):
        x[i] = j
        if i > 2:
            if ok(i):
                storeString(i)
        if i < n:
            Try(i + 1)

def solve():
    global n
    n = int(input())
    Try(1)
    res.sort(key = len)
    for x in res:
        print(x)

t = 1
# t = int(input())
for _ in range(t):
    solve()