'''
    author: htkhanh05
    created at: 27.11.2025 12:49:02
'''

def binToDec(s):
    ans = 0
    for x in s:
        ans = ans * 2 + int(x)
    return ans

def solve():
    s = input()
    i = len(s)
    ans = []
    while i > 0:
        ss = s[max(0, i - 3):i]
        ans.append(str(binToDec(ss)))
        i -= 3
    res = ''.join(reversed(ans))
    print(res)

t = 1
# t = int(input())
for _ in range(t):
    solve()