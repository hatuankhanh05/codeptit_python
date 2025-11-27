'''
    author: htkhanh05
    created at: 27.11.2025 12:38:35
'''

def isLocPhat(n):
    for c in n:
        if c != '6' and c != '8':
            return False
    return True

def isPretty(n):
    i = 0
    length = len(n)
    while i < length:
        if n[i:i + 3] == '688':
            i += 3
        elif n[i:i + 2] == '68':
            i += 2
        elif n[i] == '6':
            i += 1
        else:
            break
    return i >= length

def solve():
    n = input()
    print('YES' if isLocPhat(n) and isPretty(n) else 'NO')

t = 1
#t = int(input())
for _ in range(t):
    solve()