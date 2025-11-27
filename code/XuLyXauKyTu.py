'''
    author: htkhanh05
    created at: 27.11.2025 12:55:06
'''

def solve():
    s1 = input()
    s2 = input()
    a1 = s1.split()
    a2 = s2.split()
    a1 = [x.lower() for x in a1]
    a2 = [x.lower() for x in a2]
    a1 = list(set(a1))
    a2 = list(set(a2))
    uni = list(set(a1 + a2))
    inter = []
    for x in a1:
        if x in a2:
            inter.append(x)
    uni.sort()
    inter.sort()
    for x in uni:
        print(x, end=' ')
    print()
    for x in inter:
        print(x, end=' ')

t = 1
#t = int(input())
for _ in range(t):
    solve()