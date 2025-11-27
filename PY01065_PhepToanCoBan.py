'''
    author: htkhanh05
    created at: 26.11.2025 22:08:32
'''

def checkMatch(x, y):
    if y[0] != '?' and int(y[0]) != x // 10:
        return False
    if y[1] != '?' and int(y[1]) != x % 10:
        return False
    return True

def solve():
    s = input()
    sa = s[0:2] 
    sop = s[3]
    sb = s[5:7]
    sres = s[10:12]
    ops = ['+', '-', '*', '/']
    if sop != '?':
        ops = [sop]
    for op in ops:
        for a in range(10, 100):
            if not checkMatch(a, sa):
                continue
            for b in range(10, 100):
                if not checkMatch(b, sb):
                    continue
                res = None
                if op == '+':
                    res = a + b
                elif op == '-':
                    res = a - b
                elif op == '*':
                    res = a * b
                else:
                    if a % b != 0:
                        continue
                    res = a // b
                if res < 10 or res > 99:
                    continue
                if not checkMatch(res, sres):
                    continue
                print(f'{a} {op} {b} = {res}')
                return
    print('WRONG PROBLEM!')

t = 1
t = int(input())
for _ in range(t):
    solve()