'''
    author: htkhanh05
    created at: 17.11.2025 08:19:48
'''

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    val = None
    step = None
    for i in range(n):
        cnt = 0
        for j in range(n):
            if j == i:
                continue
            cnt += abs(arr[j] - arr[i])
        if val == None or step > cnt:
            val = arr[i]
            step = cnt
    print(step, val)

t = 1
#t = int(input())
for _ in range(t):
    solve()