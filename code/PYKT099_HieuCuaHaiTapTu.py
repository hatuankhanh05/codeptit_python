'''
    author: htkhanh05
    created at: 04.12.2025 18:46:21
'''

def solve():
    with open('DATA1.in', 'r') as f:
        set1 = set(f.read().lower().split())
    with open('DATA2.in', 'r') as f:
        set2 = set(f.read().lower().split())
    ansSet1 = sorted(set1 - set2)
    ansSet2 = sorted(set2 - set1)
    print(*ansSet1)
    print(*ansSet2)

t = 1
#t = int(input())
for _ in range(t):
    solve()