'''
    author: htkhanh05
    created at: 17.11.2025 07:59:36
'''

def solve():
    n, k = map(int, input().split())
    arr = []
    mp = {}
    for x in input().strip().split():
        if mp.get(x, False) == False:
            mp[x] = True
            arr.append(x)
    arr.sort()
    n = len(arr)
    X = [i for i in range(k)]
    while True:
        for x in X:
            print(arr[x], end=' ')
        print()
        i = k - 1
        while i >= 0 and X[i] == n - k + i:
            i -= 1
        if i < 0:
            break
        X[i] += 1
        for j in range(i + 1, k):
            X[j] = X[j - 1] + 1

t = 1
#t = int(input())
for _ in range(t):
    solve()