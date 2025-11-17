'''
    author: htkhanh05
    created at: 17.11.2025 07:46:45
'''
arr = []
mp = {}

def check(x):
    cnt = 0
    cntt = 0
    while x > 0:
        cntt += 1
        if x % 10 == 2:
            cnt += 1
        x //= 10
    return cnt * 2 > cntt

def precompute():
    global arr
    global mp
    q = [0, 1, 2]
    mp[0] = True
    mp[1] = True
    mp[2] = True
    while len(q) > 0:
        curr = q.pop(0)
        if check(curr):
            arr.append(curr)
        if len(arr) == 1000:
            break
        next1 = curr * 10 + 0
        next2 = curr * 10 + 1
        next3 = curr * 10 + 2
        if mp.get(next1, False) == False:
            q.append(next1)
            mp[next1] = True
        if mp.get(next2, False) == False:
            q.append(next2)
            mp[next2] = True    
        if mp.get(next3, False) == False:
            q.append(next3)
            mp[next3] = True    
    arr.sort()

def solve():
    N = int(input())
    for i in range(N):
        print(arr[i], end=" ")
    print()

precompute()
t = 1
t = int(input())
for _ in range(t):
    solve()