'''
    author: htkhanh05
    created at: 17.11.2025 08:24:20
'''

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    odd = []
    even = []
    for x in arr:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    even.sort(reverse=True)
    odd.sort()
    ans = []
    for idx in range(n):
        x = arr[idx]
        if x % 2 == 0:
            print(even[-1], end=' ')            
            even.pop()
        elif x % 2 != 0:
            print(odd[-1], end=' ')
            odd.pop()

t = 1
#t = int(input())
for _ in range(t):
    solve()