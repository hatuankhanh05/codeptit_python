'''
    author: htkhanh05
    created at: 24.11.2025 08:07:08
'''

def solve():
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(input())
    res = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if mat[i][j] == 'C':
                cnt += 1
        res += cnt * (cnt - 1) // 2
    for j in range(n):
        cnt = 0
        for i in range(n):
            if mat[i][j] == 'C':
                cnt += 1
        res += cnt * (cnt - 1) // 2
    print(res)

t = 1
#t = int(input())
for _ in range(t):
    solve() 