'''
    author: htkhanh05
    created at: 26.11.2025 18:21:18
'''

def solve():
    s = input()
    a = list(s)
    n = len(a)
    for i in range(n - 2, -1, -1):
        best_j = -1
        mx = -1
        for j in range(i + 1, n):
            if a[j] < a[i]:
                if best_j == -1 or s[j] > mx:
                    best_j = j
                    mx = a[j]
        if best_j != -1 and i > 0:
            a[i], a[best_j] = a[best_j], a[i]
            print(''.join(a))
            return
    print(-1)

t = 1
t = int(input())
for _ in range(t):
    solve()