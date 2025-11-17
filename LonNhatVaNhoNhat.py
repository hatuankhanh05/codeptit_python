'''
    author: htkhanh05
    created at: 17.11.2025 08:15:15
'''

def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        arr = []
        for i in range(n):
            arr.append(int(input()))
        mn = min(arr)
        mx = max(arr)
        if mn == mx:
            print('BANG NHAU')
        else:
            print(mn, mx)

t = 1
#t = int(input())
for _ in range(t):
    solve()