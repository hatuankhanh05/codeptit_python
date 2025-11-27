import math

def solve():
    a = [x.lower() for x in input().split()]
    b = [x.lower() for x in input().split()]
    mp = {}
    for x in a:
        mp[x] = True
    for x in b:
        mp[x] = True
    uni = []
    for key in mp:
        uni.append(key)
    uni.sort()
    inte = []
    mp.clear()
    for x in a:
        mp[x] = True
    has = {}
    for x in b:
        if mp.get(x, False) == True and has.get(x, False) == False:
            inte.append(x)
            has[x] = True
    inte.sort()
    for x in uni:
        print(x, end = " ")
    print()
    for x in inte:
        print(x, end = " ")

t = 1
# t = int(input())
for _ in range(t):
    solve()