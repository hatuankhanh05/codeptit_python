'''
    author: htkhanh05
    created at: 27.11.2025 12:34:03
'''

def solve():
    s1 = input().strip()
    s2 = input().strip()
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    print('YES' if s1 == s2 else 'NO')

t = 1
t = int(input().strip())
for _ in range(t):
    print(f'Test {_ + 1}:', end=' ')
    solve()