import math

has = {}
a = []

def preCal():
    for i in range(60):
        for j in range(38):
            for k in range(26):
                val = 2 ** i * 3 ** j * 5 ** k
                if val not in has:
                    has[val] = True
                    a.append(val)
    a.sort()

def binarySearch(x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def solve():
    n = int(input())
    pos = binarySearch(n)
    print(pos + 1 if pos != -1 else "Not in sequence")
    
preCal()
t = 1
t = int(input())
for _ in range(t):
    solve()