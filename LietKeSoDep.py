a = []

def isValid(x):
    y = 0
    z = x
    cnt = 0
    while x:
        cnt += 1
        d = x % 10
        if d % 2 != 0: return False
        y = y * 10 + d
        x //= 10
    if y != z: return False
    if cnt % 2 != 0: return False
    return True

def preCal():
    global a
    for x in range(22, 10**6):
        if isValid(x):
            a.append(x)

def solve():
    n = int(input().strip())
    for x in a:
        if x >= n: break
        print(x, end=" ")
    print()

preCal()
t = 1
t = int(input().strip())
for _ in range(t):
    solve()